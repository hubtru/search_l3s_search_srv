from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource

from .logic import Indexer
from .dto import (
    request_mls_index_update_model,
    corpus_model,
    document_model,
    BM25_INDEX_model,
)

ns_indexer = Namespace("indexer", validate=True)

## registration api.models
ns_indexer.models[request_mls_index_update_model.name] = request_mls_index_update_model
ns_indexer.models[corpus_model.name] = corpus_model
ns_indexer.models[document_model.name] = document_model
ns_indexer.models[BM25_INDEX_model.name] = BM25_INDEX_model

@ns_indexer.route("/test", endpoint="indexer-test")
class IndexerTest(Resource):
    def get(self):
        return {"message": "Test message of indexer-service"}, HTTPStatus.OK


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


@ns_indexer.route("/bm25-indexer", endpoint="bm25_indexer")
class PyseriniIndexer(Resource):
    @ns_indexer.expect(BM25_INDEX_model)
    @ns_indexer.response(int(HTTPStatus.CREATED), "New user was successfully created.")
    @ns_indexer.response(int(HTTPStatus.CONFLICT), "Email address is already registered.")
    @ns_indexer.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @ns_indexer.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
    def post(self):
        request_data = ns_indexer.payload
        #  = reqdata.get('name')
        idxer = Indexer()
        corpus_name = request_data.get("corpus_name")
        json_collection = request_data.get("json_collection")
        generator = request_data.get("generator")
        threads = request_data.get("threads")
        idxer.bm25_indexer(corpus_name,
                               json_collection=json_collection,
                               generator=generator,
                               threads=threads
                               )
        
        return {"corpus_name": corpus_name}, 201
        # return reqdata, 201


@ns_indexer.route("/sparse-encoder", endpoint="sparse_encoder")
class SparseIndexer(Resource):
    def post(self):
        return {"message": "Success: Sparse Encoder"}


@ns_indexer.route("/dense-encoder", endpoint="dense_encoder")
class SparseIndexer(Resource):
    def post(self):
        return {"message": "Success: Dense Encoder"}

