from flask_restx import Model, fields

query_model = Model("Query", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "indexes": fields.List(fields.String),
    "query": fields.String(required=True),
    "query_history": fields.List(fields.String, default=None),
    "nr_result": fields.Integer(min=1, default=10)
})