from flask_restx import Model, fields

dense_encoder_model = Model("Dense_Encoder", {
    "dataset_dir": fields.String,
    "dataset_json": fields.String
})

## ------------- Encode Query ---------------- ##
model_dense_encode_query_input = Model("DtpDenseEncodeQueryInput", {
    "model_name": fields.String(required=True, default="bert-base-german-cased"),
    "text": fields.String(required=True, default="Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen Übung"),
})

model_dense_encode_query_output = Model("DtoDenseEncodeQueryOutput", {
    "dense_encode": fields.List(fields.Float())
})

## ------------- Encode Dataset --------------- ##
model_dense_encode_dataset_input = Model("Dataset_Encode", {
    "model_name": fields.String(required=True, default="bert-base-german-cased"),
    "dataset_name": fields.String(required=True, default="mls-tasks"),
})

model_dense_encode_dataset_output = Model("DtoDenseEncodeDatasetOutput", {
    "message": fields.String()
})