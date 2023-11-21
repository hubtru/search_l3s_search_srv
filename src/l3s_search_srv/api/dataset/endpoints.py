from http import HTTPStatus
import os
import json
from flask_restx import Namespace, Resource
from flask import request

from .logic.mls_processor import MLSConnector, MLSCorpus
from .logic.preprocessor import dataset_json2jsonl
from l3s_search_srv.util.meta import SearchSrvMeta



ns_dataset_processor = Namespace("Dataset Processor", validate=True)

flag_show_private_endpoints = False

from .dto import dto_parameter, dto_dataset_request, dto_mls_dataset, dto_mls_object

ns_dataset_processor.models[dto_parameter.name] = dto_parameter
ns_dataset_processor.models[dto_dataset_request.name] = dto_dataset_request
ns_dataset_processor.models[dto_mls_dataset.name] = dto_mls_dataset
ns_dataset_processor.models[dto_mls_object.name] = dto_mls_object

@ns_dataset_processor.route("/mls-content-type", endpoint="mls_content_type")
class MlsContentType(Resource):
    def get(self):
        "Retrieve valid mls content type for generating corpus"
        content_type = MLSConnector.VALID_CONTENT_TYPE
        content_type_json = json.dumps(content_type)
        
        return content_type, HTTPStatus.OK


@ns_dataset_processor.route("/mls-response-dataset", endpoint="mls_response_dataset", doc=flag_show_private_endpoints)
class MlsResponseDataset(Resource):
    @ns_dataset_processor.expect(dto_mls_dataset)
    def post(self):
        request_data = ns_dataset_processor.payload
        dataset_name = request_data.get("name")
        dataset_parameters = request_data.get("parameters")
        
        mls_response = MLSConnector.get_dataset_response(dataset_name, parameters=dataset_parameters)
        mls_response_json = mls_response.json()
        return mls_response_json, HTTPStatus.CREATED


@ns_dataset_processor.route("/mls-response-object", endpoint="mls_response_object", doc=flag_show_private_endpoints)
class MlsResponseObject(Resource):
    @ns_dataset_processor.expect(dto_mls_object)
    def post(self):
        object_id = ns_dataset_processor.payload.get("object_id")
        
        mls_response = MLSConnector.get_object_response(object_id)
        mls_response_json = mls_response.json()
        
        return mls_response_json, HTTPStatus.CREATED
    

@ns_dataset_processor.route("/mls-corpus", endpoint="dataset_generator_mls", doc=flag_show_private_endpoints)
class GenerateMlsDataset(Resource):
    @ns_dataset_processor.expect(dto_mls_dataset)
    @ns_dataset_processor.response(int(HTTPStatus.CREATED), description="Successfully created json file")
    @ns_dataset_processor.response(int(HTTPStatus.BAD_REQUEST), description="Request error, e.g., wrong corpus name")
    # @ns_dataset_processor.marshal_list_with(document_model)
    def post(self):
        """retrieval mls dataset and save as json file"""
        request_data = ns_dataset_processor.payload
        dataset_name = request_data.get("name")
        dataset_parameters = request_data.get("parameters")
        
        mls_response = MLSConnector.get_dataset_response(dataset_name, parameters=dataset_parameters)
        mls_response_json = mls_response.json()
        
        # corpus_json = MLSCorpus.corpus_generator(mls_response_json)
        
        
        # res = {
        #     "message": "Success",
        #     "corpus_name": dataset_name,
        #     "context": mls_response_json.get("@context"),
        #     "dataset": mls_response_json.get("hydra:member")
        # }
        return mls_response_json, HTTPStatus.CREATED


@ns_dataset_processor.route("/json-to-jsonl-converter", 
                            endpoint="json_to_jsonl_converter",
                            doc=flag_show_private_endpoints)
class JsonToJsonl(Resource):
    @ns_dataset_processor.expect(dto_dataset_request)
    def post(self):
        dataset_name = ns_dataset_processor.payload.get("dataset_name")

        if not dataset_name:
            raise ValueError("Dataset name is empty!")
        
        result = dataset_json2jsonl(dataset_name)
        
        if result == 1:
            return {"message": "Success"}, HTTPStatus.CREATED
        else:
            return result.get("error"), result.get("code")
    

# @ns_dataset_processor.route("/get-datasets-name", endpoint="get_dataset_name")
# class GetDatasetName(Resource):
#     def get(self):
#         return {"message": "Success"}, HTTPStatus.OK

from .dto import dto_dataset_modifier_request, dto_dataset_modifier_response
ns_dataset_processor.models[dto_dataset_modifier_request.name] = dto_dataset_modifier_request
ns_dataset_processor.models[dto_dataset_modifier_response.name] = dto_dataset_modifier_response

@ns_dataset_processor.route("/dataset-modifier", endpoint="dataset_modifier", doc=flag_show_private_endpoints)
@ns_dataset_processor.doc("methods to modify the datasets")
class UpdateToDataset(Resource):
    @ns_dataset_processor.expect(dto_dataset_modifier_request)
    @ns_dataset_processor.marshal_with(dto_dataset_modifier_response)
    def put(self):
        request_data = request.json
        dataset_name = request_data["dataset"]
        doc_id = request_data["id"]
        
        datasets = SearchSrvMeta().get_datasets()
        if dataset_name not in datasets:
            raise FileNotFoundError("dataset does not exist!")
        
        dataset_path = ""
        new_doc = {}
        new_doc["id"] = doc_id
        # get the content of doc
        print(new_doc)
        
        
        status = "failed"
        response = {}
        response["message"] = f'add doc to dataset: {dataset_name} with id: {doc_id}'
        response["status"] = status
        return response
    
    # @ns_dataset_processor.expect(dto_dataset_modifier_request)
    # @ns_dataset_processor.marshal_with(dto_dataset_modifier_response)
    # def delete(self):
    #     request_data = request.json
    #     dataset_name = request_data["dataset"]
    #     doc_id = request_data["id"]
    #     response = {}
    #     status = "failed"
    #     response["status"] = status
    #     try:
    #         datasets = SearchSrvMeta().get_datasets()
    #         if dataset_name not in datasets:
    #             raise FileNotFoundError("dataset does not exist!")
            
    #         response["message"] = f'delete doc from dataset: {dataset_name} with id: {doc_id}'
            
    #         return response, HTTPStatus.OK
    #     except FileNotFoundError as e:
    #         response["message"] = e.args[0]
    #         return response, HTTPStatus.INTERNAL_SERVER_ERROR