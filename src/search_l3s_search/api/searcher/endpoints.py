from http import HTTPStatus
from flask_restx import Namespace, Resource

ns_searcher = Namespace("searcher", validate=True)


@ns_searcher.route("/test", endpoint="searcher-test")
class SearcherTest(Resource):
    def get(self):
        return {"message": "Test message of sercher-service"}, HTTPStatus.OK