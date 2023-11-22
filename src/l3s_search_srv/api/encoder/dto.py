from flask_restx import Model, fields

dto_dense_encoder = Model("DtoDenseEncoder", {
    "dataset_dir": fields.String,
    "dataset_json": fields.String
})
## ------------- Encode Updater ---------------##
dto_dense_encode_updater = Model("DtoDenseEncodeUpdater", {
    "language_model": fields.String(),
    "dataset": fields.String(),
    "state": fields.Integer(),
    # "message": fields.String()
})

dto_dense_encode_updater_list = Model("DtoDenseEncodeUpdaterList", {
    "results": fields.List(fields.Nested(dto_dense_encode_updater))
})

# ## ------------- Encode Query ---------------- ##
dto_dense_encode_query_input = Model("DtoDenseEncodeQueryInput", {
    "model_name": fields.String(required=True, default="bert-base-german-cased"),
    "text": fields.String(required=True, default="Elektrotechnik 1 Versuch 8: Wirkleistung von Wechselspannungen; Wirkleistung der Sinuswechselspannung in der praktischen Übung"),
})

dto_dense_encode_query_output = Model("DtoDenseEncodeQueryOutput", {
    "dense_encode": fields.List(fields.Float())
})

## ------------- Encode Dataset --------------- ##
dto_dense_encode_dataset_input = Model("DtoDenseEncodeDatasetInput", {
    "model_name": fields.String(required=True, default="bert-base-german-cased"),
    "dataset_name": fields.String(required=True, default="mls-tasks"),
})

dto_dense_encode_dataset_output = Model("DtoDenseEncodeDatasetOutput", {
    "message": fields.String()
})
