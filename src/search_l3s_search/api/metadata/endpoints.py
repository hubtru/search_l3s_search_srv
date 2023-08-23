"""gateway for search service from l3s"""

from http import HTTPStatus
from flask_restx import Namespace, Resource
import os

ns_metadata = Namespace(name="metadata", 
                        validate=True, 
                        description="Get functions for Meta-information for using search services")


def get_subdirs(dir):
    subdirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
    return subdirs


@ns_metadata.route('/host-name-ip', endpoint="host_name_ip")
class Host(Resource):
    def get(self):
        HostName = os.getenv("HOST_NAME")
        IPAddr = os.getenv("HOST_IP")
        return {"Host Name": HostName, "Host IP": IPAddr}, HTTPStatus.OK

@ns_metadata.route("/get-datasets")
class GetDatasets(Resource):
    def get(self):
        """Get the list of available datasets"""
        dataset_dir = os.getenv("BASE_DATASETS_PATH")
        subdirs = get_subdirs(dataset_dir)
        return {"Datasets": subdirs}, HTTPStatus.OK


@ns_metadata.route("/get-encoding-types")
class GetEncodingType(Resource):
    def get(self):
        """Get the list of available encoding types"""
        encodes_dir = os.getenv("BASE_ENCODES_PATH")
        subdirs = get_subdirs(encodes_dir)
        return {"Encoding Types": subdirs}, HTTPStatus.OK


@ns_metadata.route("/get-language-models")
class GetLanguageModels(Resource):
    def get(self):
        """Get the list of available language models"""
        encodes_dense_dir = os.path.join(os.getenv("BASE_ENCODES_PATH"), 'dense')
        subdirs = get_subdirs(encodes_dense_dir)
        return {"Language Models": subdirs}, HTTPStatus.OK


@ns_metadata.route("/get-index-methods")
class GetIndexMethod(Resource):
    def get(self):
        """Get the list of available index methods"""
        index_method = ["flat-ip", "flat-l2"]
        return {"Index Methods": index_method}, HTTPStatus.OK