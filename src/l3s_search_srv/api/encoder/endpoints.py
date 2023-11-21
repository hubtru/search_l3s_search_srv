from http import HTTPStatus
import os
from flask_restx import Namespace, Resource

from .logic import XlmRobertaDenseEncoder, BertGermanCasedDenseEncoder
from l3s_search_srv.util.meta import SearchSrvMeta

ns_encoder = Namespace("Encoder", validate=True)

from .dto import dto_dense_encoder
ns_encoder.models[dto_dense_encoder.name] = dto_dense_encoder

flag_show_private_endpoints = False

## --------------------- Test ---------------------------- ##
@ns_encoder.route("/test", endpoint="encoder_test", doc=flag_show_private_endpoints)
class EncoderTest(Resource):
    def get(self):
        encodes_path = os.getenv("BASE_ENCODES_PATH")
        return {"getenv": f"{encodes_path}",
                "correct": "/home/peng_luh/__github/search_l3s/search_l3s_search_srv/encodes"}, HTTPStatus.OK

# @ns_encoder.route("/sparse-encoder", endpoint="sparse_encoder")
# class SparseEncodeGenerator(Resource):
#     def post(self):
#         return {"message": "Success: Sparse Encoder"}


## ---------------------- Encode Updater ----------------------- ##
from .dto import dto_encode_update_response, dto_dense_encode_updater_response
ns_encoder.models[dto_encode_update_response.name] = dto_encode_update_response
ns_encoder.models[dto_dense_encode_updater_response.name] = dto_dense_encode_updater_response

@ns_encoder.route('/updater', endpoint='l3s_search_encoder_updater')
class EncodeUpdater(Resource):
    @ns_encoder.marshal_with(dto_dense_encode_updater_response)
    def get(self):
        '''update the encodings'''
        ## ----------- init encodes ----------- ##
        # get the list of not encoded datasets for different language models
        # e.g. [{'bert-base-german-cased': []}, {'xlm-roberta-base': []}]
        not_encoded_datasets = SearchSrvMeta().get_not_dense_encoded_dataset()
        results = []
        for dictionary in not_encoded_datasets:
            r = {}
            language_model, datasets = list(dictionary.items())[0]
            r["language_model"] = language_model
            r["datasets"] = datasets
            
            if datasets == []:
                r["states"] = []
                r["message"] = "Everything is up to date."
                results.append(r)
                continue
            
            r["states"] = []
            for d in datasets:
                if language_model == "bert-base-german-cased":
                    enc = BertGermanCasedDenseEncoder()
                    p = enc.dataset_encoder(d)
                    r["states"].append(p)
                elif language_model == "xlm-roberta-base":
                    enc = XlmRobertaDenseEncoder()
                    p = enc.dataset_encoder(d)
                    r["states"].append(p)
                
            r["message"] = f"Number of encoded datasets: {len(datasets)}"
            results.append(r)
            
        return {"results": results}, HTTPStatus.OK

## -------------------- Encode Query -------------------- ##
from .dto import dto_dense_encode_query_input, dto_dense_encode_query_output
ns_encoder.models[dto_dense_encode_query_input.name] = dto_dense_encode_query_input
ns_encoder.models[dto_dense_encode_query_output.name] = dto_dense_encode_query_output

@ns_encoder.route("/dense-query", endpoint="dense_encoder_query", doc=flag_show_private_endpoints)
class DenseEncodeQuery(Resource):
    @ns_encoder.response(int(HTTPStatus.CREATED), "Dense encode for the input was successfully created.")
    @ns_encoder.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Error in Input Value")
    @ns_encoder.expect(dto_dense_encode_query_input)
    @ns_encoder.marshal_with(dto_dense_encode_query_output)
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
from .dto import dto_dense_encode_dataset_input, dto_dense_encode_dataset_output
ns_encoder.models[dto_dense_encode_dataset_input.name] = dto_dense_encode_dataset_input
ns_encoder.models[dto_dense_encode_dataset_output.name] = dto_dense_encode_dataset_output

@ns_encoder.route("/dense-dataset", endpoint="dense_encoder_dataset", doc=False)
class DenseEncodeDataset(Resource):
    @ns_encoder.expect(dto_dense_encode_dataset_input)
    @ns_encoder.response(int(HTTPStatus.NOT_FOUND), description="Dataset not found")
    @ns_encoder.marshal_with(dto_dense_encode_dataset_output)
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

