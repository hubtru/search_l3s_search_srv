"""Flask CLI/Application entry point."""
import os, requests
from l3s_search_srv import create_app, db
from l3s_search_srv.util.util import get_request_url

# os.environ["BASE_DATASETS_DIR"] = os.path.join(os.getcwd(), "datasets")
# os.environ["BASE_ENCODES_DIR"] = os.path.join(os.getcwd(), "encodes")
# os.environ["BASE_INDEXES_DIR"] = os.path.join(os.getcwd(), "indexes")


app = create_app(os.getenv("FLASK_ENV", "development")) 

# @app.shell_context_processor
# def shell():
#     return {"db": db}

# # Function to be called after the first request
# @app.before_first_request
# def on_startup():
#     # Make calls to the desired endpoints
#     with app.test_client() as client:
#         ## encode update
#         encoder_request_url = get_request_url(endpoint="api.l3s_search_encoder_updater")
#         print(encoder_request_url)
#         # encoder_response = requests.get(encoder_request_url)
#         # print(encoder_response.json())
#         # ## index update
#         indexer_request_url = get_request_url(endpoint="api.l3s_search_indexer_updater")
#         print(indexer_request_url)
#         # indexer_response = requests.get(indexer_request_url)
#         # print(indexer_response.json())


# Run the app
if __name__ == '__main__':
    app.test_client().get('/')
    app.run(debug=True, host="0.0.0.0", port="9043")
    # with app.test_client() as client:
    #     ## encode update
    #     encoder_request_url = get_request_url(endpoint="api.l3s_search_encoder_updater")
    #     print(encoder_request_url)
    #     # encoder_response = requests.get(encoder_request_url)
    #     # print(encoder_response.json())
    #     # ## index update
    #     indexer_request_url = get_request_url(endpoint="api.l3s_search_indexer_updater")
    #     print(indexer_request_url)
    #     # indexer_response = requests.get(indexer_request_url)
    #     # print(indexer_response.json())