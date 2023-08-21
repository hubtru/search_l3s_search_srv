"""gateway for search service from l3s"""

from http import HTTPStatus
from flask_restx import Namespace, Resource

ns_test = Namespace(name="metadata", validate=True)


@ns_test.route("/get/")
class SearchTest(Resource):
    def get(self):
        return {"message": "Success"}, HTTPStatus.OK


