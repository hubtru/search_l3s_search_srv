"""gateway for search service from l3s"""

from http import HTTPStatus
from flask_restx import Namespace, Resource
from flask import request, url_for
import os


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
@ns_metadata.route('/host', endpoint="host")
class Host(Resource):
    def get(self):
        [host, port] = request.host.split(":")
        print(host, port)
        return {"Host URL": request.host_url}, HTTPStatus.OK


## ------------ Datasets ------------- ##
from .dto import dto_dataset, dto_dataset_list
ns_metadata.models[dto_dataset.name] = dto_dataset
ns_metadata.models[dto_dataset_list.name] = dto_dataset_list

@ns_metadata.route("/test")
class DatasetTest(Resource):
    def get(self):
        print(url_for('api.reranker_test'))
        return {"results": f"{url_for('api.reranker_test')}"}

@ns_metadata.route("/datasets", endpoint="get_datasets")
class GetDatasets(Resource):
    @ns_metadata.marshal_with(dto_dataset_list)
    def get(self):
        """Get the list of available datasets"""
        try:
            dataset_dir = os.getenv("BASE_DATASETS_PATH")
            subdirs = get_subdirs(dataset_dir)
            
            datasets = []
            for s in subdirs:
                dataset = {"name": s}
                datasets.append(dataset)
            
            print(datasets)
            response = {"results": datasets}
            return response, HTTPStatus.OK
        except ValueError as e:
            print("Internal Value Error-> %s\n" % e)
            response = {"results": None}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR


## ---------- Encoding Types ---------- ##
from .dto import dto_encode_type, dto_encode_type_list
ns_metadata.models[dto_encode_type.name] = dto_encode_type
ns_metadata.models[dto_encode_type_list.name] = dto_encode_type_list
@ns_metadata.route("/encoding-types", endpoint="encoding_types")
class GetEncodingType(Resource):
    @ns_metadata.marshal_with(dto_encode_type_list)
    def get(self):
        """Get the list of available encoding types"""
        encodes_dir = os.getenv("BASE_ENCODES_PATH")
        subdirs = get_subdirs(encodes_dir)
        
        encode_types = []
        for s in subdirs:
            encode_type = {"name": s}
            encode_types.append(encode_type)
        
        response = {"results": encode_types}
            
        return response, HTTPStatus.OK



## ------- language models ------- ##

from .dto import dto_language_model, dto_language_model_list

ns_metadata.models[dto_language_model.name] = dto_language_model
ns_metadata.models[dto_language_model_list.name] = dto_language_model_list

@ns_metadata.route("/language-models")
class GetLanguageModels(Resource):
    @ns_metadata.marshal_with(dto_language_model_list)
    def get(self):
        """Get the list of available language models"""
        encodes_dense_dir = os.path.join(os.getenv("BASE_ENCODES_PATH"), 'dense')
        subdirs = get_subdirs(encodes_dense_dir)
        
        language_models = []
        for s in subdirs:
            language_model = {"name": s}
            language_models.append(language_model)
            
        response = {"results": language_models}
        
        return response, HTTPStatus.OK


## --------- index methods --------- ##
from .dto import dto_index_method, dto_index_method_list
ns_metadata.models[dto_index_method.name] = dto_index_method
ns_metadata.models[dto_index_method_list.name] = dto_index_method_list

@ns_metadata.route("/index-methods", endpoint="metadata_index_methods")
class GetIndexMethod(Resource):
    @ns_metadata.marshal_with(dto_index_method_list)
    def get(self):
        """Get the list of available index methods"""
        index_method_dir = os.getenv("BASE_INDEXES_PATH")
        print(f'Get indexes base directory: {index_method_dir}')
            
        try:
            subdirs = get_subdirs(index_method_dir)
    
            index_methods = []
            for s in subdirs:
                index_method = {"name": s}
                index_methods.append(index_method)
            
            response = {"results": index_methods}
            
            return response, HTTPStatus.OK
        except FileNotFoundError as e:
            print("Directory not found-> %s\n" % e)
            response = {"results": [{"name": None}]}
            return response, HTTPStatus.INTERNAL_SERVER_ERROR