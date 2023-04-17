"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api



api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="1.0",
          title="L3S Search Service for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
          doc="/ui",
          authorizations=authorizations,
          )


from search_l3s_search.api.test.endpoints import ns_test
api.add_namespace(ns_test, path="/search-test")

from search_l3s_search.api.indexer.endpoints import ns_indexer
api.add_namespace(ns_indexer, path="/indexer")

from search_l3s_search.api.searcher.endpoints import ns_searcher
api.add_namespace(ns_searcher, path="/searcher")

from search_l3s_search.api.reranker.endpoints import ns_reranker
api.add_namespace(ns_reranker, path="/reranker")

from search_l3s_search.api.dataset_generator.endpoints import ns_dataset_generator
api.add_namespace(ns_dataset_generator, path="/dataset-generator")

from search_l3s_search.api.encoder.endpoints import ns_encoder
api.add_namespace(ns_encoder, path="/encoder")