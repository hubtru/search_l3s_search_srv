from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource

from .logic import Indexer
from .dto import (
    request_mls_index_update_model,
    corpus_model,
    document_model,
    bm25_indexer_input_model,
    indexer_input_model
)

ns_indexer = Namespace("indexer", validate=True)

## registration api.models
ns_indexer.models[request_mls_index_update_model.name] = request_mls_index_update_model
ns_indexer.models[corpus_model.name] = corpus_model
ns_indexer.models[document_model.name] = document_model
ns_indexer.models[bm25_indexer_input_model.name] = bm25_indexer_input_model
ns_indexer.models[indexer_input_model.name] = indexer_input_model

# @ns_indexer.route("/test", endpoint="indexer-test")
# class IndexerTest(Resource):
#     def get(self):
#         return {"message": "Test message of indexer-service"}, HTTPStatus.OK


@ns_indexer.route("/index-mls-update", endpoint="index_mls_update")
class MlsIndexUpdate(Resource):
    @ns_indexer.expect(request_mls_index_update_model)
    def post(self):
        request_data = ns_indexer.payload
        list_datasets = request_data.get("datasets")
        if list_datasets:
            for dataset in list_datasets:
                pass
        
        return {"message": "Success: MLS Index Update"}


@ns_indexer.route("/traditional-indexer/bm25", endpoint="traditional_bm25_indexer")
class PyseriniIndexer(Resource):
    @ns_indexer.expect(bm25_indexer_input_model)
    @ns_indexer.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_indexer.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_indexer.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_indexer.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        request_data = ns_indexer.payload
        #  = reqdata.get('name')
        idxer = Indexer()
        dataset_name = request_data.get("dataset_name")
        json_collection = request_data.get("json_collection")
        generator = request_data.get("generator")
        threads = request_data.get("threads")
        idxer.bm25_indexer(dataset_name,
                               json_collection=json_collection,
                               generator=generator,
                               threads=threads
                               )
        
        return {"corpus_name": dataset_name}, 201
        # return reqdata, 201


# @ns_indexer.route("/dense/hnsw", endpoint="indexer_dense_hnsw")
class HNSWIndexer(Resource):
    @ns_indexer.expect(indexer_input_model)
    def post(self):
        request_data = ns_indexer.payload
        encode_cat = request_data.get("encode_cat")
        model_name = request_data.get("model_name")
        dataset_name = request_data.get("dataset_name")
        print(request_data)
        idxer = Indexer()
        idxer.hnsw_indexer(encode_cat, model_name, dataset_name)
        return {"message": "success"}, HTTPStatus.CREATED


# @ns_indexer.route("/dense/pq", endpoint="indexer_dense_pq")
class PQIndexer(Resource):
    @ns_indexer.expect(indexer_input_model)
    def post(self):
        request_data = ns_indexer.payload
        encode_cat = request_data.get("encode_cat")
        model_name = request_data.get("model_name")
        dataset_name = request_data.get("dataset_name")
        print(request_data)
        idxer = Indexer()
        idxer.pq_indexer(encode_cat, model_name, dataset_name)
        return {"message": "success"}, HTTPStatus.CREATED
    

@ns_indexer.route("/dense/flat", endpoint="indexer_dense_flatl2")
class FlatL2Indexer(Resource):
    
    @ns_indexer.expect(indexer_input_model)
    def post(self):
        """service for flat indexing"""
        request_data = ns_indexer.payload
        encode_type = request_data.get("encode_type")
        model_name = request_data.get("model_name")
        index_method = request_data.get("index_method")
        dataset_name = request_data.get("dataset_name")
        
        if index_method not in ["flat-l2", "flat-ip"]:
            raise ValueError("Wrong index method")
        
        idxer = Indexer()
        idxer.flat(encode_type, model_name, index_method, dataset_name)
        return {"message": "success"}, HTTPStatus.CREATED
    


