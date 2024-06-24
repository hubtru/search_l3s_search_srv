import os, requests
import sys
from http import HTTPStatus
import json
from flask import jsonify, request
from flask import current_app as app
from flask_restx import Namespace, Resource, reqparse
from pprint import pprint
from .dto import (
    dto_simple_search_request, dto_simple_search_response
)
from .logic import Searcher, EmbeddingCustomizer
from l3s_search_srv.util.util import get_request_url, dirs_pruning
from l3s_search_srv.util.meta import SearchSrvMeta
from transformers import AutoTokenizer

ns_searcher = Namespace("searcher", validate=True)

ns_searcher.models[dto_simple_search_request.name] = dto_simple_search_request
ns_searcher.models[dto_simple_search_response.name] = dto_simple_search_response

## ------------ config: sse_search_client --------------- ##
import swagger_client

sse_search_config = swagger_client.Configuration()
sse_search_config.host = os.getenv("SSE_SEARCH_HOST")
print("*" * 80)
print("sse-search-host: ", sse_search_config.host)
print("*" * 80)

client_sse_search = swagger_client.ApiClient(sse_search_config)
sse_search_user_api = swagger_client.UserApi(client_sse_search)
sse_search_learning_profile_api = swagger_client.LearningProfilesApi(client_sse_search)
sse_search_learning_history_api = swagger_client.LearningHistoryApi(client_sse_search)
sse_search_learning_unit_api = swagger_client.LearningUnitsApi(client_sse_search)
sse_search_learning_path_api = swagger_client.LearningPathApi(client_sse_search)
sse_search_skill_api = swagger_client.SkillApi(client_sse_search)

# @ns_searcher.route("/test", endpoint="searcher-test")
# class SearcherTest(Resource):
#     def get(self):
#         return {"message": "Test message of sercher-service"}, HTTPStatus.OK

## ------------------------- Secret Checker ------------------------ ##
parser_secret = reqparse.RequestParser()
parser_secret.add_argument('secret_key', type=str, location='args')


@ns_searcher.route('/check_secret')
class CheckSecretKey(Resource):
    @ns_searcher.expect(parser_secret)
    def get(self):
        request_data = parser_secret.parse_args()
        if request_data["secret_key"] == os.getenv('L3S_API_KEY'):
            return {"message": "valid secret key"}, HTTPStatus.OK
        else:
            return {"message": "invalid secret key"}, HTTPStatus.BAD_REQUEST


## ------------------------- Searcher Updater ------------------------ ##
from datetime import datetime
from .dto import dto_document, dto_document_list, dto_searcher_update_response

ns_searcher.models[dto_document.name] = dto_document
ns_searcher.models[dto_document_list.name] = dto_document_list
ns_searcher.models[dto_searcher_update_response.name] = dto_searcher_update_response


# @ns_searcher.hide
@ns_searcher.route('/searcher-update', endpoint="searcher_update")
class SearcherUpdate(Resource):
    @ns_searcher.expect(dto_document_list)
    @ns_searcher.marshal_with(dto_searcher_update_response)
    def post(self):
        '''update the serch service'''
        try:
            ## Get the data from payload
            request_data = request.json
            # pprint(request_data)
            ns_searcher.logger.info("Starting: Checking client secret...")
            # print(request_data["secret"])
            if request_data["secret"] != os.getenv('L3S_API_KEY'):
                raise ValueError("Invalid secret key!")

            ns_searcher.logger.info("Success: client secret valid.")
            list_documents = request_data["documents"]

            ## if empty list -> return ok
            if list_documents == []:
                raise ValueError("Empty list of documents")

            ## save the file to ./datasets
            ## create the file and directory
            ns_searcher.logger.info("Creating file name and directory...")
            file_name = "data.json"
            dataset_name = f"documents_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            save_to = os.path.join(os.getenv("BASE_DATASETS_DIR"), dataset_name)

            ## check whether the directory already exists
            if not os.path.exists(save_to):
                # If it doesn't exist, create the directory
                os.makedirs(save_to)
                ns_searcher.logger.info(f"Directory '{save_to}' created.")
            else:
                ## if exists, raise error
                print(f"Directory '{save_to}' already exists.")
                raise FileExistsError("Confilict: Directory already exists.")

            ns_searcher.logger.info("Success: file name and directory created.")

            ns_searcher.logger.info("Starting: Save the new dataset to the directory...")
            file_dir = os.path.join(save_to, file_name)
            with open(file_dir, 'w') as file:
                json.dump(list_documents, file, indent=4)
            ns_searcher.logger.info("Success: New dataset saved...")

            ## Encoding: encode the new dataset
            ns_searcher.logger.info("Starting: Encoding dataset...")
            encoder_request_url = get_request_url(endpoint="api.l3s_search_encoder_updater")
            encoder_response = requests.get(encoder_request_url)
            print(f"encoder response: {encoder_response.json()}")
            ns_searcher.logger.info("Success: dataset encoded.")

            ## Indexing: index the new dataset
            ns_searcher.logger.info("Starting: Indexing the new dataset...")
            indexer_request_url = get_request_url(endpoint="api.l3s_search_indexer_updater")
            indexer_response = requests.get(indexer_request_url)
            print(f"indexer response: {indexer_response.json()}")
            ns_searcher.logger.info("Success: Dataset indexed.")

            ## remove old files
            ### check if new dataset is ready
            check_new_dataset = SearchSrvMeta().check_new_dataset(dataset_name)
            ns_searcher.logger.info(f"Check Dataset: {check_new_dataset}")

            flags = list(check_new_dataset.values())
            new_dataset_is_ready = all(element == 1 for element in flags)

            if new_dataset_is_ready:
                ### remove old datesets
                ns_searcher.logger.info("Starting: Removing old dataset...")
                dirs_pruning(os.getenv("BASE_DATASETS_DIR"))
                ns_searcher.logger.info("Success: Old dataset removed.")

                ### remove old encodings
                ns_searcher.logger.info("Starting: Removing old encoding data...")
                for l in SearchSrvMeta().LANGUAGE_MODELS:
                    target_dir = os.path.join(os.getenv("BASE_ENCODES_DIR"), f'dense/{l}')
                    dirs_pruning(target_dir)
                ns_searcher.logger.info("Success: Old encoding data removed.")

                ### remove old indexes
                ns_searcher.logger.info("Starting: Removing old index files...")
                for i in SearchSrvMeta().INDEX_METHODS:
                    target_dir = os.path.join(os.getenv("BASE_INDEXES_DIR"), i)
                    dirs_pruning(target_dir)
                ns_searcher.logger.info("Success: Old index files removed.")

                return {"message": "New Dataset is ready"}, HTTPStatus.CREATED
            else:
                raise ImportError("Failed to update dataset")
        except KeyError as e:
            return {"message": e.args[0]}, HTTPStatus.BAD_REQUEST
        except ValueError as e:
            return {"message": "Empty list of documents."}, HTTPStatus.BAD_REQUEST
        except FileExistsError as e:
            return {"message": e.args[0]}, HTTPStatus.INTERNAL_SERVER_ERROR
        except ImportError as e:
            return {"message": e.args[0]}, HTTPStatus.CONFLICT
        ## ---------------------------------------------------------------------------------

        # return {"message": "data received"}, HTTPStatus.CREATED


## ----------------------- Dense Retrieval ---------------------- ##
from l3s_search_srv.util.meta import SearchSrvMeta

from .dto import dto_dense_search_request, dto_dense_search_response, dto_dense_search_response_list

ns_searcher.models[dto_dense_search_request.name] = dto_dense_search_request
ns_searcher.models[dto_dense_search_response.name] = dto_dense_search_response
ns_searcher.models[dto_dense_search_response_list.name] = dto_dense_search_response_list


@ns_searcher.route("/dense-retrieval", endpoint="dense_retrieval")
class DenseRetrieval(Resource):
    @ns_searcher.expect(dto_dense_search_request)
    @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_searcher.marshal_with(dto_dense_search_response_list)
    def post(self):
        """Semantic Search using dense retrieval"""
        request_data = request.json
        user_id = request_data.get("user_id")
        orga_id = request_data.get("owner")
        query = request_data.get("query")
        use_skill_profile = request_data.get("use_skill_profile")
        use_learning_profile = request_data.get("user_learning_profile")
        language_model = request_data.get("language_model")
        index_method = request_data.get("index_method")
        entity_type = request_data.get("entity_type")
        nr_result = request_data.get("nr_result")

        try:
            dataset_name = SearchSrvMeta().get_latest_dataset()

            # print(dataset_name)
            if dataset_name == "" or dataset_name is None:
                raise FileExistsError("No dataset")

            embeddingCustomizer = EmbeddingCustomizer()
            results = embeddingCustomizer.add_after(
                query,
                use_skill_profile,
                use_learning_profile,
                user_id,
                language_model,
                dataset_name,
                index_method
            )

            # filter result type
            if entity_type != "all":
                if entity_type in ["task", "skill", "path"]:
                    key_to_check = "entity_type"
                    results = [d for d in results if d.get(key_to_check) == entity_type]
                else:
                    raise ValueError('Invalid entity type.')

            if nr_result != 0:
                results = results[:nr_result]

            ns_searcher.logger.info(f"Results:\n{results}")

            response = {"message": "success", "results": results}
            return response, HTTPStatus.CREATED

        except ValueError as e:
            return {"results": [], "message": e.args[0]}, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileExistsError as e:
            return {"results": [], "message": e.args[0]}, HTTPStatus.NOT_FOUND


@ns_searcher.route("/traditional-retrieval", endpoint="traditional_retrieval", doc=False)
class SimpleSearch(Resource):
    @ns_searcher.expect(dto_simple_search_request)
    @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        request_data = request.json
        # print(type(request_data))
        query = request_data.get("query")
        dataset_name = request_data.get("dataset")
        index_name = request_data.get("index")

        searcher = Searcher(os.getenv("BASE_INDEXES_DIR"))
        results = searcher.traditional_retrieval(
            query,
            dataset_name=dataset_name,
            index_name=index_name
        )

        ## individualization
        company_id = request_data.get("cid")
        user_id = request_data.get("uid")
        if company_id:
            ## filtering based on company
            pass

        if user_id:
            ## filtering based on user's query history
            pass

        return results

# @ns_searcher.route("/sparse-retrieval", endpoint="sparse_retrieval")
# class SparseRetrieval(Resource):
#     @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
#     @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
#     @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
#     @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
#     def post(self):
#         return {"message": "Success: Sparse Retrieval"}


# @ns_searcher.route("/hybrid-retrieval", endpoint="hybrid_retrieval")
# class HybridRetrieval(Resource):
#     @ns_searcher.expect(input_dense_search_model)
#     @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
#     @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
#     @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
#     @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
#     def post(self):
#         request_data = request.json
#         language_model = request_data.get("language_model")
#         index_method = request_data.get("index_method")
#         dataset_name = request_data.get("dataset_name")
#         query = request_data.get("query")
#         nr_result = request_data.get("nr_result")

#         searcher = Searcher(os.getenv("BASE_INDEXES_DIR"))
#         results = []

#         return request_data, HTTPStatus.OK
