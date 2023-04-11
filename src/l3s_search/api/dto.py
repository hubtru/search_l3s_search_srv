from flask_restx import Model, fields

query_model = Model("Query", {
    "UID": fields.String(),
    "CID": fields.String(),
    "query": fields.String(),
    "query_history": fields.List(fields.String()),
})