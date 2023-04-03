from http import HTTPStatus
from flask_restx import Namespace, Resource

ns_indexer = Namespace("indexer", validate=True)


@ns_indexer.route("/test", endpoint="indexer-test")
class IndexerTest(Resource):
    def get(self):
        return {"message": "Test message of indexer-service"}, HTTPStatus.OK