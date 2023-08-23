"""Flask app initialization via factory pattern."""
import os

from flask import Flask, redirect
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from search_l3s_search.config import get_config

import os, socket

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
    
    # os.environ["HOST_NAME"] = socket.gethostname()
    # os.environ["HOST_IP"] = socket.gethostbyname(os.getenv("HOST_NAME"))
    
    
    @app.route('/')
    def index():
        return redirect(f"http://{os.getenv('HOST_IP')}:{os.getenv('L3S_SEARCH_PORT')}/l3s-search/", code=200) 
    
    # to avoid a circular import
    from search_l3s_search.api import api_bp
    
    app.register_blueprint(api_bp)
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    return app
