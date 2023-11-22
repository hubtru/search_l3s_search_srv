import os, requests
from http import HTTPStatus
import json
from flask import jsonify, request
from flask import current_app as app
from flask_restx import Namespace, Resource
from pprint import pprint
from .dto import (
    dto_simple_search_request, dto_simple_search_response
)
from .logic import Searcher
from l3s_search_srv.util.util import get_request_url

ns_searcher = Namespace("searcher", validate=True)

ns_searcher.models[dto_simple_search_request.name] = dto_simple_search_request
ns_searcher.models[dto_simple_search_response.name] = dto_simple_search_response


# @ns_searcher.route("/test", endpoint="searcher-test")
# class SearcherTest(Resource):
#     def get(self):
#         return {"message": "Test message of sercher-service"}, HTTPStatus.OK


## ------------------------- Searcher Updater ------------------------ ##
from datetime import datetime
from .dto import dto_document, dto_document_list
ns_searcher.models[dto_document.name] = dto_document
ns_searcher.models[dto_document_list.name] = dto_document_list
@ns_searcher.route('/searcher-update', endpoint="searcher_update")
class SearcherUpdate(Resource):
    @ns_searcher.expect(dto_document_list)
    def post(self):
        '''update the serch service'''
        request_data = request.json
        list_documents = request_data["documents"]
        
        if list_documents == []:
            return {"message": "empty list of documents."}, HTTPStatus.OK
        
        
        ## save the file to ./datasets
        file_name = "data.json"
        formatted_time = datetime.now().strftime("%Y%m%d%H%M%S")
        save_to = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"documents_{formatted_time}")
        if not os.path.exists(save_to):
            # If it doesn't exist, create the directory
            os.makedirs(save_to)
            print(f"Directory '{save_to}' created.")
        else:
            print(f"Directory '{save_to}' already exists.")
        
        file_dir = os.path.join(save_to, file_name)
        
        with open(file_dir, 'w') as file:
            json.dump(list_documents, file, indent=4)
        
        ## encode the new dataset
        encoder_request_url = get_request_url(endpoint="api.l3s_search_encoder_updater")
        print(encoder_request_url)
        encoder_response = requests.get(encoder_request_url)
        print(encoder_response.json())
        ## index the new dataset
        indexer_request_url = get_request_url(endpoint="api.l3s_search_indexer_updater")
        indexer_response = requests.get(indexer_request_url)
        print(indexer_response.json())
        
        
        return {"message": "data received"}, HTTPStatus.CREATED






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
        use_learning_profile = request_data.get("use_learning_profile")
        language_model = request_data.get("language_model")
        index_method = request_data.get("index_method")
        entity_type = request_data.get("entity_type")
        nr_result = request_data.get("nr_result")
        
        try:
            dataset_name = SearchSrvMeta().get_latest_dataset()
            print(dataset_name)
            if dataset_name == "" or dataset_name == None:
                raise FileExistsError("No dataset") 
        
            # print(request_data)
            if not use_skill_profile and not use_learning_profile:
                ## case 1: not using skill profile and learning profile
                
                # print(os.getenv("BASE_INDEXES_PATH"))
                searcher = Searcher()
                results = searcher.dense_retrieval(
                    query=query,
                    language_model=language_model,
                    dataset_name=dataset_name,
                    index_method=index_method
                )
                pprint(results[0])
                    
                if entity_type != "all":
                    if entity_type in ["task", "skill", "path"]:
                        key_to_check = "entity_type"
                        results = [d for d in results if d.get(key_to_check) == entity_type]
                    else:
                        raise ValueError('Invalid entity type.')
                        
                if nr_result != 0:
                    results = results[:nr_result]
                    
                # print("results")
                response = {"results": results}
                # response = results
                    
                return response, HTTPStatus.CREATED
        
            elif not use_skill_profile and use_learning_profile:
                ## case 2: not using skill profile but using learning profile
                # get the learning profile of the user
                print("*** case 2: not using skill profile but using learning profile ***")
                return {"results": [], "message": "case 2 not implemented"}, HTTPStatus.OK
            elif use_skill_profile and not use_learning_profile:
                ## case 3: using skill profile but not learning profile
                # get the skill profile of the user
                print("*** case 3: using skill profile but not learning profile ***")
                return {"results": [], "message": "case 3 not implemented"}, HTTPStatus.OK
            else:
                ## case 4: using both skill profile and learning profile
                # get the skill and learning profile of the user
                print("*** case 4: using both skill profile and learning profile ***")
                return {"results": [], "message": "case 4 not implemented"}, HTTPStatus.OK
            
        except ValueError as e:
            return {"results": [], "message": e.args[0]}, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileExistsError as e:
            return {"results": [], "message": e.args[0]}, HTTPStatus.NOT_FOUND
            








# @ns_searcher.route("/traditional-retrieval", endpoint="traditional_retrieval")
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

        searcher = Searcher(os.getenv("BASE_INDEXES_PATH"))
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
        
#         searcher = Searcher(os.getenv("BASE_INDEXES_PATH"))
#         results = []
        
#         return request_data, HTTPStatus.OK



