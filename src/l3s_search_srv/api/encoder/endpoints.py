from http import HTTPStatus
import os
from flask_restx import Namespace, Resource

from .logic import XlmRobertaDenseEncoder, BertGermanCasedDenseEncoder
from l3s_search_srv.util.meta import SearchSrvMeta

ns_encoder = Namespace("Encoder", validate=True)

from .dto import dense_encoder_model
ns_encoder.models[dense_encoder_model.name] = dense_encoder_model

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


## -------------------- Encode Query -------------------- ##
from .dto import model_dense_encode_query_input, model_dense_encode_query_output
ns_encoder.models[model_dense_encode_query_input.name] = model_dense_encode_query_input
ns_encoder.models[model_dense_encode_query_output.name] = model_dense_encode_query_output

@ns_encoder.route("/dense-query", endpoint="dense_encoder_query")
class DenseEncodeQuery(Resource):
    @ns_encoder.response(int(HTTPStatus.CREATED), "Dense encode for the input was successfully created.")
    @ns_encoder.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Error in Input Value")
    @ns_encoder.expect(model_dense_encode_query_input)
    @ns_encoder.marshal_with(model_dense_encode_query_output)
    def post(self):
        
        input_data = ns_encoder.payload.get("text")
        model_name = ns_encoder.payload.get("model_name")
        
        try:
            if input_data:
                if model_name == "bert-base-german-cased":
                    enc = BertGermanCasedDenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                else:
                    raise ValueError("********* Error: Invalid Language Model *********")
            
            response = {"dense_encode": dense_vector_list}
            
            return response, HTTPStatus.CREATED
        except ValueError as e:
            print(e.args[0])
            response = {"dense_encode": []}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR


## ---------------- Encode Dataset ----------------- ##
from .dto import model_dense_encode_dataset_input
ns_encoder.models[model_dense_encode_dataset_input.name] = model_dense_encode_dataset_input
@ns_encoder.route("/dense-dataset", endpoint="dense_encoder_dataset")
class DenseEncodeDataset(Resource):
    @ns_encoder.expect(model_dense_encode_dataset_input)
    @ns_encoder.response(int(HTTPStatus.NOT_FOUND), description="Dataset not found")
    def post(self):
        model_name = ns_encoder.payload.get("model_name")
        dataset_name = ns_encoder.payload.get("dataset_name")
        
        search_serv_meta = SearchSrvMeta()
        print(search_serv_meta.get_datasets())
        
        if model_name == "bert-base-german-cased":
            enc = BertGermanCasedDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "xlm-roberta-base":
            enc = XlmRobertaDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
            
            
        if p == HTTPStatus.NOT_FOUND:
            return {"message": "file not found"}, p
        
        return {"message": search_serv_meta.ENCODE_METHODS}, HTTPStatus.CREATED
        
        
    
    
# request_data = ns_encoder.payload
# dataset_dir = request_data.get("dataset_dir")
# dataset_json = request_data.get("dataset_json")
# dataset_path_rel = "datasets/" + dataset_dir + "/" + dataset_json
# dataset_path_abs = os.path.join(os.getenv("ROOT_PATH"), dataset_path_rel)
# path_output_dir = os.path.join(os.getenv("ROOT_PATH"), "encodes/dense_encoder")
# enc = Encoder()
# p = enc.dense_encoder(dataset_path_abs, path_output_dir)