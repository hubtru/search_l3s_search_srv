from flask_restx import Model, fields

dense_encoder_model = Model("Dense_Encoder", {
    "dataset_dir": fields.String,
    "dataset_json": fields.String
})