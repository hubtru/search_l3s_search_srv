from flask_restx import Model, fields

model_dataset = Model("DtoDataset", {
    "name": fields.String(description="name of dataset", default=None),
})

model_dataset_list = Model("DtoDatasetList", {
    "results": fields.List(fields.Nested(model_dataset))
})

model_encode_type = Model("DtoEncodeType", {
    "name": fields.String(description="name of encode type", default=None)
})

model_encode_type_list = Model("DtoEncodeTypeList", {
    "results": fields.List(fields.Nested(model_encode_type))
})

model_language_model = Model("DtoLanguageModel", {
    "name": fields.String(description="name of language model", default=None)
})

model_language_model_list = Model("DtoLanguageModelList", {
    "results": fields.List(fields.Nested(model_language_model))
})

model_index_method = Model("DtoIndexMethod", {
    "name": fields.String(description="name of index method", default=None)
})

model_index_method_list = Model("DtoIndexMethodList", {
    "results": fields.List(fields.Nested(model_index_method))
})


model_host = Model("DtoHost", {
    "host": fields.String(),
    "port": fields.String(),
    "host_url": fields.Url()
})