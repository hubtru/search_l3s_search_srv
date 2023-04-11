from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource

from search_l3s_search.api.indexer.logic import Indexer
from search_l3s_search.api.indexer.dto import corpus

ns_indexer = Namespace("indexer", validate=True)

corpus_model = ns_indexer.model("Corpus", corpus)

@ns_indexer.route("/test", endpoint="indexer-test")
class IndexerTest(Resource):
    def get(self):
        return {"message": "Test message of indexer-service"}, HTTPStatus.OK


@ns_indexer.route("/indexer-pyserini")
class PyseriniIndexer(Resource):
    @ns_indexer.expect(corpus_model)
    def post(self):
        reqdata = ns_indexer.payload
        corpus_name = reqdata.get('name')
        # idxer = Indexer()
        # idxer.pyserini_indexer(corpus_name=corpus_name)
        
        return {"corpus_name": corpus_name}, 201
        # return reqdata, 201
