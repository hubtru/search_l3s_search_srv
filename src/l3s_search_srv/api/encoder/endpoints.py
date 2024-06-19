from http import HTTPStatus
import os
from flask_restx import Namespace, Resource


from .logic import CrossRobertaSentenceTransformerEncoder, XlmRobertaDenseEncoder, BertGermanCasedDenseEncoder, \
    DeBERTaDenseEncoder, BertGermanUncasedDenseEncoder, BertMultiLingualUncasedDenseEncoder, \
    BertMultiLingualCasedDenseEncoder, NVEmbedDenseEncoder, LLama3DenseEncoder, E5LargeMultiLingualDenseEncoder
from l3s_search_srv.util.meta import SearchSrvMeta

ns_encoder = Namespace("Encoder", validate=True)

from .dto import dto_dense_encoder
ns_encoder.models[dto_dense_encoder.name] = dto_dense_encoder


@ns_encoder.route("/encodings", endpoint="l3s_search_encodings")
class EncoderTest(Resource):
    def get(self):
        '''get existing encodings'''
        try:
            dense_encodings = SearchSrvMeta().get_existing_dense_encodings()
            return {"message": "success", "encodings": dense_encodings}, HTTPStatus.OK
        except ValueError as e:
            return {"message": e.args[0], "encodings": []}, HTTPStatus.INTERNAL_SERVER_ERROR
        

# from .dto import dto_encoded_datasets, dto_encoded_datasets_list
# ns_metadata.models[dto_encoded_datasets.name] = dto_encoded_datasets
# ns_metadata.models[dto_encoded_datasets_list.name] = dto_encoded_datasets_list

# @ns_metadata.route('/encodings', endpoint='l3s_search_metadata_encodings')
# class Encodings(Resource):
#     @ns_metadata.marshal_with(dto_encoded_datasets_list)
#     def get(self):
#         '''get list of existing encodings'''
#         results = SearchSrvMeta().get_existing_dense_encodings()
#         return {"results": results}, HTTPStatus.OK


## ---------------------- Encode Updater ----------------------- ##
from .dto import dto_dense_encode_updater, dto_dense_encode_updater_list
ns_encoder.models[dto_dense_encode_updater.name] = dto_dense_encode_updater
ns_encoder.models[dto_dense_encode_updater_list.name] = dto_dense_encode_updater_list

@ns_encoder.route('/updater', endpoint='l3s_search_encoder_updater', doc=False)
class EncodeUpdater(Resource):
    @ns_encoder.marshal_with(dto_dense_encode_updater_list)
    @ns_encoder.response(int(HTTPStatus.OK), description="Success")
    @ns_encoder.response(int(HTTPStatus.NOT_FOUND), description="No datasets found.")
    def get(self):
        '''update the encodings'''
        ## ----------- init encodes ----------- ##
        # get the list of not encoded datasets for different language models
        # e.g. [{'bert-base-german-cased': []}, {'xlm-roberta-base': []}]
        try:
            existing_datasets = SearchSrvMeta().get_datasets()
            if existing_datasets == []:
                raise FileNotFoundError('No Datasets found.')

            # get not encoded datasets
            not_encoded_datasets = SearchSrvMeta().get_not_dense_encoded_datasets()
            
            results = []
            for dictionary in not_encoded_datasets:
                r = {}
                language_model, datasets = list(dictionary.items())[0]
                r["language_model"] = language_model
                # r["datasets"] = datasets
                
                if datasets == []:
                    r["dataset"] = "Everything is up to date."
                    r["state"] = 2
                    # r["message"] = ""
                    results.append(r)
                    continue
                
                for d in datasets:
                    r["dataset"] = d
                    if language_model == "bert-base-german-cased":
                        enc = BertGermanCasedDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "xlm-roberta-base":
                        enc = XlmRobertaDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "cross-en-de-roberta-sentence-transformer":
                        enc = CrossRobertaSentenceTransformerEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "geberta-xlarge":
                        enc = DeBERTaDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "bert-base-german-uncased":
                        enc = BertGermanUncasedDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "bert-base-multilingual-uncased":
                        enc = BertMultiLingualUncasedDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "bert-base-multilingual-cased":
                        enc = BertMultiLingualCasedDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "NV-Embed-v1":
                        enc = NVEmbedDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "Meta-Llama-3-8B":
                        enc = LLama3DenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    elif language_model == "multilingual-e5-large":
                        enc = E5LargeMultiLingualDenseEncoder()
                        p = enc.dataset_encoder(d)
                        r["state"] = p
                    
                    results.append(r)
                
            return {"results": results}, HTTPStatus.OK
        except FileNotFoundError as e:
            results = {"language_model": "N.A.", "dataset": e.args[0], "state": -1}
            return {"results": results}, HTTPStatus.NOT_FOUND
        


## -------------------- Encode Query -------------------- ##
from .dto import dto_dense_encode_query_input, dto_dense_encode_query_output
ns_encoder.models[dto_dense_encode_query_input.name] = dto_dense_encode_query_input
ns_encoder.models[dto_dense_encode_query_output.name] = dto_dense_encode_query_output

@ns_encoder.route("/dense-query", endpoint="dense_encoder_query", doc=False)
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
                elif model_name == "xlm-roberta-base":
                    enc = XlmRobertaDenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "cross-en-de-roberta-sentence-transformer":
                    enc = CrossRobertaSentenceTransformerEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "geberta-xlarge":
                    enc = DeBERTaDenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "bert-base-german-uncased":
                    enc = BertGermanUncasedDenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "bert-base-multilingual-uncased":
                    enc = BertMultiLingualUncasedDenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "bert-base-multilingual-cased":
                    enc = BertMultiLingualCasedDenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "NV-Embed-v1":
                    enc = NVEmbedDenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "Meta-Llama-3-8B":
                    enc = LLama3DenseEncoder()
                    dense_vector_list = enc.query_encoder(input_data)
                elif model_name == "multilingual-e5-large":
                    enc = E5LargeMultiLingualDenseEncoder()
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
        # print(search_serv_meta.get_datasets())
        
        if model_name == "bert-base-german-cased":
            enc = BertGermanCasedDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "xlm-roberta-base":
            enc = XlmRobertaDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "cross-en-de-roberta-sentence-transformer":
            enc = CrossRobertaSentenceTransformerEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "geberta-xlarge":
            enc = DeBERTaDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "bert-base-german-uncased":
            enc = BertGermanUncasedDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "bert-base-multilingual-uncased":
            enc = BertMultiLingualUncasedDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "bert-base-multilingual-cased":
            enc = BertMultiLingualCasedDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "NV-Embed-v1":
            enc = NVEmbedDenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "Meta-Llama-3-8B":
            enc = LLama3DenseEncoder()
            p = enc.dataset_encoder(dataset_name)
        elif model_name == "multilingual-e5-large":
            enc = E5LargeMultiLingualDenseEncoder()
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

