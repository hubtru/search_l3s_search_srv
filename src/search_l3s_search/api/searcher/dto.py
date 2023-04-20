from flask_restx import Model, fields

query_model = Model("Query", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "dataset": fields.String,
    "index": fields.String,
    "query": fields.String(required=True),
    "nr_result": fields.Integer(min=1, default=10)
})

input_dense_search_model = Model("Dense_Searcher_Input", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "query": fields.String(required=True),
    "index_method": fields.String,
    "dataset_name": fields.String,
    "nr_result": fields.Integer(min=1, default=10)
})