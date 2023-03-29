"""API blueprint configuration"""
from flask import Blueprint
from flask_restx import Api

from search_l3s_search.api.test.endpoints import ns_test

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}


api = Api(api_bp,
          version="1.0",
          title="L3S Search Service for SEARCH",
          description="Welcome to the Swagger UI documentation site!",
          doc="/ui",
          authorizations=authorizations,
          )

api.add_namespace(ns_test, path="/search-test")

