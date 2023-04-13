from flask_restx import Model, fields

dataset_model = Model("Dataset", {
    "name": fields.String,
})