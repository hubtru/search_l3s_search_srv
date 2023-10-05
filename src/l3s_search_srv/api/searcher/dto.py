from flask_restx import Model, fields

dto_simple_search_request = Model("DtoSimpleSearchRequest", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "dataset": fields.String,
    "index": fields.String,
    "query": fields.String(required=True),
    "nr_result": fields.Integer(min=1, default=10)
})

dto_simple_search_response = Model("DtoSimpleSearchResponse", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "id": fields.String(),
})

dto_dense_search_request = Model("DtoDenseSearchRequest", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "query": fields.String(required=True, default="Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen \u00dcbung"),
    "language_model": fields.String(default="bert-base-german-cased"),
    "index_method": fields.String(default="flat-l2"),
    "dataset_name": fields.String(default="mls-tasks"),
    "nr_result": fields.Integer(min=1, default=10)
})

dto_dense_search_response = Model("DtoDenseSearchResponse", {
    "uid": fields.String(description="user ID", default=None),
    "cid": fields.String(description="company ID", default=None),
    "id": fields.String(),
    "similarity": fields.Float(attribute='cosine_similarity')
})

dto_dense_search_response_list = Model("DtoDenseSearchResponseList",{
    "results": fields.List(fields.Nested(dto_dense_search_response))
})