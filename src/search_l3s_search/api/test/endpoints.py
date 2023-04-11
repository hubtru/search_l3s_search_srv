"""gateway for search service from l3s"""

from http import HTTPStatus
from flask_restx import Namespace, Resource

ns_test = Namespace(name="test", validate=True)


@ns_test.route("/search-test")
class SearchTest(Resource):
    def get(self):
        return {"message": "Success"}, HTTPStatus.OK


