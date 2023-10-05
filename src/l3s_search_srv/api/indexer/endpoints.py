from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource

from .logic import Indexer
from .dto import (
    dto_mls_index_update_request,
    dto_corpus,
    dto_document,
    dto_bm25_indexer_request,
    dto_indexer_request,
    dto_indexer_response)

ns_indexer = Namespace("indexer", validate=True)

## registration api.models
ns_indexer.models[dto_indexer_request.name] = dto_indexer_request
ns_indexer.models[dto_indexer_response.name] = dto_indexer_response
ns_indexer.models[dto_mls_index_update_request.name] = dto_mls_index_update_request
ns_indexer.models[dto_corpus.name] = dto_corpus
ns_indexer.models[dto_document.name] = dto_document
ns_indexer.models[dto_bm25_indexer_request.name] = dto_bm25_indexer_request

# @ns_indexer.route("/test", endpoint="indexer-test")
# class IndexerTest(Resource):
#     def get(self):
#         return {"message": "Test message of indexer-service"}, HTTPStatus.OK


@ns_indexer.route("/index-mls-update", endpoint="index_mls_update")
class MlsIndexUpdate(Resource):
    @ns_indexer.expect(dto_mls_index_update_request)
    def post(self):
        request_data = ns_indexer.payload
        list_datasets = request_data.get("datasets")
        if list_datasets:
            for dataset in list_datasets:
                pass
        
        return {"message": "Success: MLS Index Update"}


@ns_indexer.route("/traditional/bm25", endpoint="traditional_bm25_indexer")
class PyseriniIndexer(Resource):
    @ns_indexer.expect(dto_bm25_indexer_request)
    @ns_indexer.response(int(HTTPStatus.CREATED), "index file was successfully created.")
    @ns_indexer.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_indexer.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_indexer.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        request_data = ns_indexer.payload
        #  = reqdata.get('name')
        # idxer = Indexer()
        # dataset_name = request_data.get("dataset_name")
        # json_collection = request_data.get("json_collection")
        # generator = request_data.get("generator")
        # threads = request_data.get("threads")
        # idxer.bm25_indexer(dataset_name,
        #                        json_collection=json_collection,
        #                        generator=generator,
        #                        threads=threads
        #                        )
        
        # return {"corpus_name": dataset_name}, 201
        return {"status": "working...", "request data": request_data}
        # return reqdata, 201


# @ns_indexer.route("/dense/hnsw", endpoint="indexer_dense_hnsw")
class HNSWIndexer(Resource):
    @ns_indexer.expect(dto_indexer_request)
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
    @ns_indexer.expect(dto_indexer_request)
    def post(self):
        request_data = ns_indexer.payload
        encode_cat = request_data.get("encode_cat")
        model_name = request_data.get("model_name")
        dataset_name = request_data.get("dataset_name")
        print(request_data)
        idxer = Indexer()
        idxer.pq_indexer(encode_cat, model_name, dataset_name)
        return {"message": "success"}, HTTPStatus.CREATED
    


@ns_indexer.route("/dense/flat", endpoint="indexer_dense_flat")
class FlatL2Indexer(Resource):
    @ns_indexer.response(int(HTTPStatus.CREATED), "Index file was successfully created.")
    # @ns_indexer.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    # @ns_indexer.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_indexer.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    @ns_indexer.expect(dto_indexer_request)
    @ns_indexer.marshal_with(dto_indexer_response)
    def post(self):
        """service for flat indexing"""
        request_data = ns_indexer.payload
        
        encode_type = request_data.get("encode_type")
        model_name = request_data.get("model_name")
        index_method = request_data.get("index_method")
        dataset_name = request_data.get("dataset_name")

        try:
            idxer = Indexer()
            idxer.flat(encode_type, model_name, index_method, dataset_name)
            return {"message": "dataset is indexed successfully"}, HTTPStatus.CREATED
        except ValueError as e:
            return {"message": e.args[0]}, HTTPStatus.INTERNAL_SERVER_ERROR
    


