from http import HTTPStatus
from flask_restx import Namespace, Resource

from .dto import dataset_model
from .logic import MLSConnector

ns_dataset_generator = Namespace("dataset-generator", validate=True)
ns_dataset_generator.models[dataset_model.name] = dataset_model

@ns_dataset_generator.route("/mls", endpoint="dataset_generator_mls")
class GenerateMlsDataset(Resource):
    @ns_dataset_generator.expect(dataset_model)
    @ns_dataset_generator.response(int(HTTPStatus.CREATED), description="Successfully created json file")
    @ns_dataset_generator.response(int(HTTPStatus.BAD_REQUEST), description="Request error, e.g., wrong corpus name")
    # @ns_dataset_generator.marshal_list_with(document_model)
    def post(self):
        """retrieval mls dataset and save as json file"""
        request_data = ns_dataset_generator.payload
        dataset_name = request_data.get("name")
        connector = MLSConnector()
        mls_response = connector.get_response(dataset_name)
        mls_response_json = mls_response.json()
        
        res = {
            "message": "Success",
            "corpus_name": dataset_name,
            "context": mls_response_json.get("@context"),
            "dataset": mls_response_json.get("hydra:member")
        }
        return res, HTTPStatus.CREATED