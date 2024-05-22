"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api



api_bp = Blueprint("api", __name__, url_prefix="/l3s-search")
# authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="1.1.0",
          title="L3S Search Service for SEARCH",
          description="Welcome to the Swagger UI documentation site test!",
          #   doc="/ui",
          #   authorizations=authorizations,
          )


from l3s_search_srv.api.test.endpoints import ns_test
api.add_namespace(ns_test, path="/search-test")

from l3s_search_srv.api.metadata.endpoints import ns_metadata
api.add_namespace(ns_metadata, path="/metadata")

# from l3s_search_srv.api.dataset.endpoints import ns_dataset_processor
# api.add_namespace(ns_dataset_processor, path="/dataset-processor")

from l3s_search_srv.api.encoder.endpoints import ns_encoder
api.add_namespace(ns_encoder, path="/encoder")

from l3s_search_srv.api.indexer.endpoints import ns_indexer
api.add_namespace(ns_indexer, path="/indexer")

from l3s_search_srv.api.searcher.endpoints import ns_searcher
api.add_namespace(ns_searcher, path="/searcher")

from l3s_search_srv.api.reranker.endpoints import ns_reranker
api.add_namespace(ns_reranker, path="/reranker")

