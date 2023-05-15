from flask_restx import Model, fields

dense_encoder_model = Model("Dense_Encoder", {
    "dataset_dir": fields.String,
    "dataset_json": fields.String
})

input_encode_query_model = Model("Query_Encode", {
    "model_name": fields.String(required=True, default="bert-base-german-cased"),
    "text": fields.String(required=True),
})

input_encode_dataset_model = Model("Dataset_Encode", {
    "model_name": fields.String(required=True, default="bert-base-german-cased"),
    "dataset_name": fields.String(required=True),
})