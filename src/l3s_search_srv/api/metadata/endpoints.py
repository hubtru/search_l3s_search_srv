"""gateway for search service from l3s"""

from http import HTTPStatus
from flask_restx import Namespace, Resource
from flask import request, url_for, jsonify
import os

from l3s_search_srv.util.meta import SearchSrvMeta

ns_metadata = Namespace(name="Metadata", 
                        validate=True, 
                        description="Get functions for Meta-information for using search services")

def get_subdirs(dir):
    try:
        subdirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
        return subdirs
    except ValueError as e:
        return e
    

from .dto import dto_host
ns_metadata.models[dto_host.name] = dto_host
@ns_metadata.route('/host', endpoint="host", doc=False)
class Host(Resource):
    def get(self):
        [host, port] = request.host.split(":")
        print(host, port)
        return {"Host URL": request.host_url}, HTTPStatus.OK


## ------------ Datasets ------------- ##
from .dto import dto_dataset_list
ns_metadata.models[dto_dataset_list.name] = dto_dataset_list

@ns_metadata.route("/datasets", endpoint="get_datasets")
class GetDatasets(Resource):
    @ns_metadata.marshal_with(dto_dataset_list)
    @ns_metadata.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), description="Internal value error")
    @ns_metadata.response(int(HTTPStatus.NOT_FOUND), description="Path not found")
    def get(self):
        """Get the datasets"""
        try:
            datasets = SearchSrvMeta().get_datasets()
            response = {"results": datasets}
            return response, HTTPStatus.OK
        except ValueError as e:
            print("Value Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR
        except FileNotFoundError as e:
            print(e.args[0])
            response = {"results": None}
            return response, HTTPStatus.NOT_FOUND

## -------------------- Encoding Types -------------------- ##
from .dto import dto_encode_type_list
ns_metadata.models[dto_encode_type_list.name] = dto_encode_type_list
@ns_metadata.route("/encoding-types", endpoint="encoding_types")
class GetEncodingType(Resource):
    @ns_metadata.marshal_with(dto_encode_type_list)
    @ns_metadata.response(int(HTTPStatus.OK), description="Success")
    @ns_metadata.response(int(HTTPStatus.BAD_REQUEST), description="Value error")
    @ns_metadata.response(int(HTTPStatus.NOT_FOUND), description="Path not found")
    @ns_metadata.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), description="Unknown internal error")
    def get(self):
        """Get the list of available encoding types"""
        try:
            encode_methods = SearchSrvMeta().get_encode_methods()
            response = {"results": encode_methods}
            return response, HTTPStatus.OK
        except ValueError as e:
            print("Value Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.BAD_REQUEST
        except FileNotFoundError as e:
            print(e.args[0])
            response = {"results": None}
            return response, HTTPStatus.NOT_FOUND
        except Exception as e:
            print("Internal Server Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR


## ------------------------ language models --------------------------- ##

from .dto import dto_language_model_list
ns_metadata.models[dto_language_model_list.name] = dto_language_model_list

@ns_metadata.route("/language-models")
class GetLanguageModels(Resource):
    @ns_metadata.marshal_with(dto_language_model_list)
    @ns_metadata.response(int(HTTPStatus.OK), description="Success")
    @ns_metadata.response(int(HTTPStatus.BAD_REQUEST), description="Value error")
    @ns_metadata.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), description="Unknown internal error")
    def get(self):
        """Get the list of available language models"""
        try:
            language_models = SearchSrvMeta().LANGUAGE_MODELS
            response = {"results": language_models}
            return response, HTTPStatus.OK
        except ValueError as e:
            print("Value Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.BAD_REQUEST
        except Exception as e:
            print("Internal Server Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR


## --------- index methods --------- ##
from .dto import dto_index_method, dto_index_method_list
ns_metadata.models[dto_index_method.name] = dto_index_method
ns_metadata.models[dto_index_method_list.name] = dto_index_method_list

@ns_metadata.route("/index-methods", endpoint="l3s_search_metadata_index_methods")
class GetIndexMethod(Resource):
    @ns_metadata.marshal_with(dto_index_method_list)
    @ns_metadata.response(int(HTTPStatus.OK), description="Success")
    @ns_metadata.response(int(HTTPStatus.BAD_REQUEST), description="Value error")
    @ns_metadata.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), description="Unknown internal error")
    def get(self):
        """Get the list of available index methods"""
        try:
            index_methods = SearchSrvMeta().INDEX_METHODS
            return {"results": index_methods}
        except ValueError as e:
            print("Value Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.BAD_REQUEST
        except Exception as e:
            print("Internal Server Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR