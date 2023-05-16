from http import HTTPStatus
import os
from flask_restx import Namespace, Resource

from .logic import XlmRobertaDenseEncoder, BertGermanCasedDenseEncoder
from .dto import (
    dense_encoder_model,
    input_encode_query_model,
    input_encode_dataset_model
)

ns_encoder = Namespace("encoder", validate=True)

ns_encoder.models[dense_encoder_model.name] = dense_encoder_model
ns_encoder.models[input_encode_query_model.name] = input_encode_query_model
ns_encoder.models[input_encode_dataset_model.name] = input_encode_dataset_model

@ns_encoder.route("/test", endpoint="encoder_test")
class EncoderTest(Resource):
    def get(self):
        encodes_path = os.getenv("BASE_ENCODES_PATH")
        return {"getenv": f"{encodes_path}",
                "correct": "/home/peng_luh/__github/search_l3s/search_l3s_search_srv/encodes"}, HTTPStatus.OK


@ns_encoder.route("/sparse-encoder", endpoint="sparse_encoder")
class SparseEncodeGenerator(Resource):
    def post(self):
        return {"message": "Success: Sparse Encoder"}


@ns_encoder.route("/dense-encoder/query", endpoint="dense_encoder_xml_roberta_query")
class DenseEncodeQuery(Resource):
    @ns_encoder.expect(input_encode_query_model)
    def post(self):
        
        input_data = ns_encoder.payload.get("text")
        if input_data:
            enc = BertGermanCasedDenseEncoder()
            dense_vector_list = enc.query_encoder(input_data)
        
        return {"dense encode": dense_vector_list}, HTTPStatus.CREATED
    

@ns_encoder.route("/dense-encoder/dataset", endpoint="dense_encode_dataset")
class DenseEncodeDataset(Resource):
    @ns_encoder.expect(input_encode_dataset_model)
    @ns_encoder.response(int(HTTPStatus.NOT_FOUND), description="Dataset not found")
    def post(self):
        model_name = ns_encoder.payload.get("model_name")
        dataset_name = ns_encoder.payload.get("dataset_name")
        
        if model_name == "bert-base-german-cased":
            enc = BertGermanCasedDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "xlm-roberta-base":
            enc = XlmRobertaDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
            
            
        if p == HTTPStatus.NOT_FOUND:
            return {"message": "file not found"}, p
        
        return {"message": p}, HTTPStatus.CREATED
        
        
    
    
# request_data = ns_encoder.payload
# dataset_dir = request_data.get("dataset_dir")
# dataset_json = request_data.get("dataset_json")
# dataset_path_rel = "datasets/" + dataset_dir + "/" + dataset_json
# dataset_path_abs = os.path.join(os.getenv("ROOT_PATH"), dataset_path_rel)
# path_output_dir = os.path.join(os.getenv("ROOT_PATH"), "encodes/dense_encoder")
# enc = Encoder()
# p = enc.dense_encoder(dataset_path_abs, path_output_dir)