from http import HTTPStatus
import os
from flask_restx import Namespace, Resource

from .logic import Encoder
from .dto import dense_encoder_model

ns_encoder = Namespace("encoder", validate=True)

ns_encoder.models[dense_encoder_model.name] = dense_encoder_model


@ns_encoder.route("/test", endpoint="encoder_test")
class EncoderTest(Resource):
    def get(self):
        return {"message": "Success: Encoder Test"}, HTTPStatus.OK


@ns_encoder.route("/sparse-encoder", endpoint="sparse_encoder")
class SparseEncoder(Resource):
    def post(self):
        return {"message": "Success: Sparse Encoder"}


@ns_encoder.route("/dense-encoder", endpoint="dense_encoder")
class DenseEncoder(Resource):
    @ns_encoder.expect(dense_encoder_model)
    def post(self):
        request_data = ns_encoder.payload
        dataset_dir = request_data.get("dataset_dir")
        dataset_json = request_data.get("dataset_json")
        dataset_path_rel = "datasets/" + dataset_dir + "/" + dataset_json
        dataset_path_abs = os.path.join(os.getenv("ROOT_PATH"), dataset_path_rel)
        path_output_dir = os.path.join(os.getenv("ROOT_PATH"), "encodes/dense_encoder")
        enc = Encoder()
        p = enc.dense_encoder(dataset_path_abs, path_output_dir)
        
        return {"message": p}