"""Flask CLI/Application entry point."""
import os

from search_l3s_search import create_app, db

os.environ["ROOT_PATH"] = os.getcwd()

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db}

