import os, requests
from http import HTTPStatus
import json
from flask import jsonify, request
from flask import current_app as app
from flask_restx import Namespace, Resource, reqparse
from pprint import pprint
from .dto import (
    dto_simple_search_request, dto_simple_search_response
)
from .logic import Searcher
from l3s_search_srv.util.util import get_request_url, dirs_pruning
from l3s_search_srv.util.meta import SearchSrvMeta
from transformers import AutoTokenizer

ns_searcher = Namespace("searcher", validate=True)

ns_searcher.models[dto_simple_search_request.name] = dto_simple_search_request
ns_searcher.models[dto_simple_search_response.name] = dto_simple_search_response

## ------------ config: sse_search_client --------------- ##
from swagger_client import sse_search_client
sse_search_config = sse_search_client.Configuration()
sse_search_config.host = os.getenv("SSE_SEARCH_HOST")
print("*"*80)
print("sse-search-host: ", sse_search_config.host)
print("*"*80)

client_sse_search = sse_search_client.ApiClient(sse_search_config)
sse_search_user_api = sse_search_client.UserApi(client_sse_search)
sse_search_learning_profile_api = sse_search_client.LearningProfilesApi(client_sse_search)
sse_search_learning_history_api = sse_search_client.LearningHistoryApi(client_sse_search)
sse_search_learning_unit_api = sse_search_client.LearningUnitsApi(client_sse_search)
sse_search_skill_api = sse_search_client.SkillApi(client_sse_search)
sse_search_learning_path_api = sse_search_client.LearningPathApi(client_sse_search)

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
        if request_data["secret_key"] == os.getenv('MLS_CLIENT_SECRET'):
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
            pprint(request_data)
            ns_searcher.logger.info("Starting: Checking client secret...")
            print(request_data["secret"])
            if request_data["secret"] != os.getenv('MLS_CLIENT_SECRET'):
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
            if dataset_name == "" or dataset_name == None:
                raise FileExistsError("No dataset")
            searcher = Searcher()


            if not use_skill_profile and not use_learning_profile:
                ## case 1: not using skill profile and learning profile
                ns_searcher.logger.info("*** case 1: not using skill profile and learning profile ***")
                # !!No need to change anything in the query!!
                pass

            elif not use_skill_profile and use_learning_profile:
                ## case 2: not using skill profile but using learning profile
                ns_searcher.logger.info("*** case 2: not using skill profile but using learning profile ***")

                # retrieve user specific data
                user = sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
                ns_searcher.logger.info(f"User Info: {user}")

                learning_profile_id = user["learning_profile"]
                if learning_profile_id is '':
                    raise ValueError("User has no learningProfile")

                learning_profile = sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(learning_profile_id).to_dict()
                ns_searcher.logger.info(f"Learning Profile Info: {learning_profile}")

                learning_history_id = learning_profile["learning_history_id"]
                if learning_history_id is '':
                    raise ValueError("Learning profile of user has no learning history")

                learning_history = sse_search_learning_history_api.learning_history_controller_get_learning_history(learning_history_id).to_dict()
                ns_searcher.logger.info(f"Learning History Info: {learning_history}")

                started_learning_units = learning_history["started_learning_units"]
                started_learning_paths = learning_history["personal_paths"]
                learned_skills = learning_history["learned_skills"]

                # retrieve skills relevant to query
                relevant_skills = []
                for started_unit_id in started_learning_units:
                    learning_unit = sse_search_learning_unit_api.search_learning_unit_controller_get_learning_unit(started_unit_id).to_dict()

                    teachingGoals = learning_unit["teaching_goals"]
                    requiredSkills = learning_unit["required_skills"]

                    check_already_learned = lambda x: x in learned_skills
                    teachingGoals = list(filter(check_already_learned, teachingGoals))
                    requiredSkills = list(filter(check_already_learned, requiredSkills))
                    all_skills = teachingGoals + requiredSkills
                    learned_skills += all_skills

                    relevant_skills += [sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict() for skill_to_learn in all_skills]

                for started_path_id in started_learning_paths:
                    learning_path = sse_search_learning_path_api.learning_path_mgmt_controller_get_learning_path(
                        started_path_id).to_dict()

                    check_already_learned = lambda x: x in relevant_skills
                    path_goals = learning_path["path_goals"]
                    path_goals = list(filter(check_already_learned, path_goals))

                    requirements = learning_path["requirements"]
                    requirements = list(filter(check_already_learned, requirements))

                    all_skills = path_goals + requirements

                    learned_skills += all_skills
                    relevant_skills += [sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict()
                                        for skill_to_learn in all_skills]
                ns_searcher.logger.info(f"Relevant Skills: {relevant_skills}")

                # get seperator token. Is it needed?
                sep_token = AutoTokenizer.from_pretrained(searcher.language_models[language_model]).sep_token

                # add skill names to query
                ns_searcher.logger.info(f"Original Query: {query}")
                for skill in relevant_skills:
                    query += f"{sep_token}{skill['name']}"
                ns_searcher.logger.info(f"Final Query: {query}")

            elif use_skill_profile and not use_learning_profile:
                ## case 3: using skill profile but not learning profile
                ns_searcher.logger.info("*** case 3: using skill profile but not learning profile ***")

                # retrieve user specific data
                user = sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
                ns_searcher.logger.info(f"User Info: {user}")

                learning_profile_id = user["learning_profile"]
                if learning_profile_id is '':
                    raise ValueError("User has no learningProfile")

                learning_profile = sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                    learning_profile_id).to_dict()
                ns_searcher.logger.info(f"Learning Profile Info: {learning_profile}")

                learning_history_id = learning_profile["learning_history_id"]
                if learning_history_id is '':
                    raise ValueError("Learning profile of user has no learning history")

                learning_history = sse_search_learning_history_api.learning_history_controller_get_learning_history(
                    learning_history_id).to_dict()
                ns_searcher.logger.info(f"Learning History Info: {learning_history}")

                learned_skills = learning_history["learned_skills"]

                # retrieve skills relevant to query
                relevant_skills = [sse_search_skill_api.skill_mgmt_controller_get_skill(skill).to_dict() for skill in learned_skills]
                ns_searcher.logger.info(f"Relevant Skills: {relevant_skills}")

                # get seperator token. Is it needed?
                sep_token = AutoTokenizer.from_pretrained(searcher.language_models[language_model]).sep_token

                # add skill names to query
                ns_searcher.logger.info(f"Original Query: {query}")
                for skill in relevant_skills:
                    query += f"{sep_token}{skill['name']}"
                ns_searcher.logger.info(f"Final Query: {query}")

            else:
                ## case 4: using both skill profile and learning profile
                ns_searcher.logger.info("*** case 4: using both skill profile and learning profile ***")

                # retrieve user specific data
                user = sse_search_user_api.user_mgmt_controller_get_user_profiles(user_id).to_dict()
                ns_searcher.logger.info(f"User Info: {user}")

                learning_profile_id = user["learning_profile"]
                if learning_profile_id is '':
                    raise ValueError("User has no learningProfile")

                learning_profile = sse_search_learning_profile_api.learning_profile_controller_get_learning_profile_by_id(
                    learning_profile_id).to_dict()
                ns_searcher.logger.info(f"Learning Profile Info: {learning_profile}")

                learning_history_id = learning_profile["learning_history_id"]
                if learning_history_id is '':
                    raise ValueError("Learning profile of user has no learning history")

                learning_history = sse_search_learning_history_api.learning_history_controller_get_learning_history(
                    learning_history_id).to_dict()
                ns_searcher.logger.info(f"Learning History Info: {learning_history}")

                started_learning_units = learning_history["started_learning_units"]
                started_learning_paths = learning_history["personal_paths"]
                learned_skills = learning_history["learned_skills"]

                # retrieve skills relevant to query
                relevant_skills = [sse_search_skill_api.skill_mgmt_controller_get_skill(skill).to_dict() for skill in learned_skills]
                for started_unit_id in started_learning_units:
                    learning_unit = sse_search_learning_unit_api.search_learning_unit_controller_get_learning_unit(
                        started_unit_id).to_dict()

                    teachingGoals = learning_unit[
                        "teaching_goals"]
                    requiredSkills = learning_unit[
                        "required_skills"]

                    check_already_learned = lambda x: x in learned_skills
                    teachingGoals = list(filter(check_already_learned, teachingGoals))
                    requiredSkills = list(filter(check_already_learned, requiredSkills))
                    all_skills = teachingGoals + requiredSkills
                    learned_skills += all_skills

                    relevant_skills += [sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict()
                                        for skill_to_learn in all_skills]

                for started_path_id in started_learning_paths:
                    learning_path = sse_search_learning_path_api.learning_path_mgmt_controller_get_learning_path(
                        started_path_id).to_dict()

                    check_already_learned = lambda x: x in relevant_skills
                    path_goals = learning_path["path_goals"]
                    path_goals = list(filter(check_already_learned, path_goals))

                    requirements = learning_path["requirements"]
                    requirements = list(filter(check_already_learned, requirements))

                    all_skills = path_goals + requirements

                    learned_skills += all_skills
                    relevant_skills += [sse_search_skill_api.skill_mgmt_controller_get_skill(skill_to_learn).to_dict()
                                        for skill_to_learn in all_skills]
                ns_searcher.logger.info(f"Relevant Skills: {relevant_skills}")

                # get seperator token. Is it needed?
                sep_token = AutoTokenizer.from_pretrained(searcher.language_models[language_model]).sep_token

                # add skill names to query
                ns_searcher.logger.info(f"Original Query: {query}")
                for skill in relevant_skills:
                    query += f"{sep_token}{skill['name']}"
                ns_searcher.logger.info(f"Final Query: {query}")

            results = searcher.dense_retrieval(
                query=query,
                language_model=language_model,
                dataset_name=dataset_name,
                index_method=index_method
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
            ns_searcher.logger.info(f"Results: {results}")

            response = {"message": "success", "results": results}
            return response, HTTPStatus.CREATED

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



