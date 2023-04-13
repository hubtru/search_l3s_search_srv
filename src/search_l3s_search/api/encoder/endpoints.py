from http import HTTPStatus
from flask_restx import Namespace, Resource

ns_encoder = Namespace("encoder", validate=True)

@ns_encoder.route("/test", endpoint="encoder_test")
class EncoderTest(Resource):
    def get(self):
        return {"message": "Success: Encoder Test"}, HTTPStatus.OK