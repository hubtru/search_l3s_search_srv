from http import HTTPStatus
from flask import jsonify, request
from flask import current_app as app
from flask_restx import Namespace, Resource

from .dto import query_model
from .logic import Searcher

ns_searcher = Namespace("searcher", validate=True)

ns_searcher.models[query_model.name] = query_model

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
        print(index_name)
        searcher = Searcher(app.config["BASE_PATH_INDEXES"])
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
    @ns_searcher.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_searcher.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_searcher.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_searcher.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        return {"message": "Success: Dense Retrieval"}