from flask_restx import Model, fields

dto_simple_search_request = Model("DtoSimpleSearchRequest", {
    "user_id": fields.String(description="user ID", default=None),
    "owner": fields.String(description="company ID", default=None),
    "dataset": fields.String,
    "index": fields.String,
    "query": fields.String(required=True),
    "nr_result": fields.Integer(min=1, default=10)
})

dto_simple_search_response = Model("DtoSimpleSearchResponse", {
    "user_id": fields.String(description="user ID", default=None),
    "owner": fields.String(description="company ID", default=None),
    "id": fields.String(),
})

dto_dense_search_request = Model("DtoDenseSearchRequest", {
    "user_id": fields.String(description="user ID", default=None),
    "owner": fields.List(fields.String(), description="company ID", default=None),
    "query": fields.String(required=True, default="Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen \u00dcbung"),
    "use_skill_profile": fields.Boolean(default=False),
    "user_learning_profile": fields.Boolean(default=False),
    "language_model": fields.String(default="bert-base-german-cased"),
    "index_method": fields.String(enum=["flat-l2", "flat-ip"], default="flat-l2"),
    "entity_type": fields.String(enum=["all", "skill", "path", "task"]),
    "nr_result": fields.Integer(min=0)
})

dto_dense_search_response = Model("DtoDenseSearchResponse", {
    "user_id": fields.String(description="user ID", default=None),
    "owner": fields.String(description="company ID", default=None),
    "entity_id": fields.String(),
    "entity_type": fields.String(),
    "similarity": fields.Float(attribute='cosine_similarity')
})

dto_dense_search_response_list = Model("DtoDenseSearchResponseList",{
    "message": fields.String(),
    "results": fields.List(fields.Nested(dto_dense_search_response)),
})


dto_document = Model("DtoDocument", {
    "id": fields.Integer(),
    "owner": fields.List(fields.String(), description="List of orga-id"),
    "entity_id": fields.String(),
    "entity_id_full": fields.String(),
    "entity_type": fields.String(enum=["skill", "path", "task"]),
    "contents": fields.String()
})


dto_document_list = Model("DtoDocumentList", {
    "secret": fields.String(),
    "documents": fields.List(fields.Nested(dto_document))
})

dto_searcher_update_response = Model("DtoSearcherUpdateResponse", {
    "message": fields.String()
})