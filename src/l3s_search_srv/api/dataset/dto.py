from flask_restx import Model, fields

dto_parameter = Model("DtoParameter", {
    "parameter_name": fields.String(description="mls-api parameter")
})

dto_mls_dataset = Model("DtoMlsDataset", {
    "name": fields.String(description="description: dataset name, e.g., tasks, documents"),
    "parameters": fields.List(fields.Nested(dto_parameter), description="List of mls-api parameters"),
})

dto_mls_object = Model("DtoMlsObject", {
    "object_id": fields.String()
})


dto_dataset_request = Model("DtoDatasetRequest", {
    "dataset_name": fields.String(required=True),
})