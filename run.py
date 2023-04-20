"""Flask CLI/Application entry point."""
import os

from search_l3s_search import create_app, db


# os.environ["BASE_DATASETS_PATH"] = os.path.join(os.getcwd(), "datasets")
# os.environ["BASE_ENCODES_PATH"] = os.path.join(os.getcwd(), "encodes")
# os.environ["BASE_INDEXES_PATH"] = os.path.join(os.getcwd(), "indexes")



app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db}

