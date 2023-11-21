"""Flask app initialization via factory pattern."""
import os

from flask import Flask, redirect, request, url_for
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from l3s_search_srv.config import get_config
import os, socket
from pprint import pprint
from l3s_search_srv.util.meta import SearchSrvMeta

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    
    # set envs
    os.environ["BASE_PATH"] = os.getcwd()
    os.environ["BASE_DATASETS_PATH"] = os.path.join(os.getcwd(), "datasets")
    os.environ["BASE_ENCODES_PATH"] = os.path.join(os.getcwd(), "encodes")
    os.environ["BASE_INDEXES_PATH"] = os.path.join(os.getcwd(), "indexes")
    
    path_checker = SearchSrvMeta().check_dirs()
    pprint(path_checker)
    
    
    # os.environ["HOST_NAME"] = socket.gethostname()
    # os.environ["HOST_IP"] = socket.gethostbyname(os.getenv("HOST_NAME"))

    ## ----------- update encodes ----------- ##
    
    # not_encoded_datasets = SearchSrvMeta().get_not_dense_encoded_dataset()
    # print(not_encoded_datasets)
    
    # from l3s_search_srv.api.encoder.logic import BertGermanCasedDenseEncoder, XlmRobertaDenseEncoder
    # for i in not_encoded_datasets:
    #     print(type(i))
    #     language_model, datasets = list(i.items())[0]
    #     print((language_model))
    #     print(datasets)
    #     for d in datasets:
    #         if language_model == "bert-base-german-cased":
    #             enc = BertGermanCasedDenseEncoder()
    #             p = enc.dataset_encoder(d)
    #         elif language_model == "xlm-roberta-base":
    #             enc = XlmRobertaDenseEncoder()
    #             p = enc.dataset_encoder(d)
    
    ## --------------- init indexes --------------- ##
         

    @app.route('/')
    def index():
        return redirect(f"{request.host_url}l3s-search/", code=200) 
    
    # to avoid a circular import
    from l3s_search_srv.api import api_bp
    
    app.register_blueprint(api_bp)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    return app
