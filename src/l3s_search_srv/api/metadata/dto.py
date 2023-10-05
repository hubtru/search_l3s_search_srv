from flask_restx import Model, fields

dto_dataset = Model("DtoDataset", {
    "name": fields.String(description="name of dataset", default=None),
})

dto_dataset_list = Model("DtoDatasetList", {
    "results": fields.List(fields.Nested(dto_dataset))
})

dto_encode_type = Model("DtoEncodeType", {
    "name": fields.String(description="name of encode type", default=None)
})

dto_encode_type_list = Model("DtoEncodeTypeList", {
    "results": fields.List(fields.Nested(dto_encode_type))
})

dto_language_model = Model("DtoLanguageModel", {
    "name": fields.String(description="name of language model", default=None)
})

dto_language_model_list = Model("DtoLanguageModelList", {
    "results": fields.List(fields.Nested(dto_language_model))
})

dto_index_method = Model("DtoIndexMethod", {
    "name": fields.String(description="name of index method", default=None)
})

dto_index_method_list = Model("DtoIndexMethodList", {
    "results": fields.List(fields.Nested(dto_index_method))
})

dto_host = Model("DtoHost", {
    "host": fields.String(),
    "port": fields.String(),
    "host_url": fields.Url()
})