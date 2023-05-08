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
    "query": fields.String(required=True, default="Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen \u00dcbung"),
    "language_model": fields.String(default="bert-german-uncased"),
    "index_method": fields.String(default="flat-l2"),
    "dataset_name": fields.String(default="mls-tasks"),
    "nr_result": fields.Integer(min=1, default=10)
})