from flask_restx import Model, fields

query_model = Model("Query", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "dataset": fields.String,
    "index": fields.String,
    "query": fields.String(required=True),
    "nr_result": fields.Integer(min=1, default=10)
})