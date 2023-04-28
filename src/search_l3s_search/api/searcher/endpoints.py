import os
from http import HTTPStatus
from flask import jsonify, request
from flask import current_app as app
from flask_restx import Namespace, Resource

from .dto import query_model, input_dense_search_model
from .logic import Searcher

ns_searcher = Namespace("searcher", validate=True)

ns_searcher.models[query_model.name] = query_model
ns_searcher.models[input_dense_search_model.name] = input_dense_search_model

@ns_searcher.route("/test", endpoint="searcher-test")
class SearcherTest(Resource):
    def get(self):
        return {"message": "Test message of sercher-service"}, HTTPStatus.OK


@ns_searcher.route("/traditional-retrieval", endpoint="traditional_retrieval")
class SimpleSearch(Resource):
    @ns_searcher.expect(query_model)
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


@ns_searcher.route("/sparse-retrieval", endpoint="sparse_retrieval")
class SparseRetrieval(Resource):
    @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        return {"message": "Success: Sparse Retrieval"}


@ns_searcher.route("/dense-retrieval", endpoint="dense_retrieval")
class DenseRetrieval(Resource):
    @ns_searcher.expect(input_dense_search_model)
    @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        request_data = request.json
        language_model = request_data.get("language_model")
        index_method = request_data.get("index_method")
        dataset_name = request_data.get("dataset_name")
        query = request_data.get("query")
        nr_result = request_data.get("nr_result")
        
        searcher = Searcher(os.getenv("BASE_INDEXES_PATH"))
        results = searcher.dense_retrieval(
            query=query,
            language_model=language_model,
            dataset_name=dataset_name,
            index_method=index_method,
            num_results=nr_result
        )
        
        return results, HTTPStatus.OK
    

@ns_searcher.route("/hybrid-retrieval", endpoint="hybrid_retrieval")
class DenseRetrieval(Resource):
    @ns_searcher.expect(input_dense_search_model)
    @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        request_data = request.json
        language_model = request_data.get("language_model")
        index_method = request_data.get("index_method")
        dataset_name = request_data.get("dataset_name")
        query = request_data.get("query")
        nr_result = request_data.get("nr_result")
        
        searcher = Searcher(os.getenv("BASE_INDEXES_PATH"))
        results = []
        
        return request_data, HTTPStatus.OK
