from http import HTTPStatus
from flask import jsonify, request
from flask import current_app as app
from flask_restx import Namespace, Resource

from .dto import query_model
from .logic import SimpleSearcher

ns_searcher = Namespace("searcher", validate=True)

ns_searcher.models[query_model.name] = query_model

@ns_searcher.route("/test", endpoint="searcher-test")
class SearcherTest(Resource):
    def get(self):
        return {"message": "Test message of sercher-service"}, HTTPStatus.OK


@ns_searcher.route("/simple-search", endpoint="simple_search")
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
        index_name = request_data.get("indexes")
        print(index_name)
        searcher = SimpleSearcher(app.config["BASE_PATH_INDEXES"])
        results = dict()
        if index_name:
            for i in index_name:
                results[i] = searcher.sparse_retrieval(query, i)
        # send request__data to searcher
        # results = searcher()
        return results