from flask_restx import Model, fields
# from search_l3s_search.api.indexer import ns_indexer

dto_corpus = Model("DtoCorpus", {
    "name": fields.String()
})

dto_document = Model("DtoDocument", {
    "id": fields.String,
    "content": fields.String,
})

dto_mls_index_update_request = Model("DtoMLSIndexUpdateRequest", {
    "datasets": fields.List(fields.String),
})

dto_bm25_indexer_request = Model("DtoBM25IndexerRequest", {
    "dataset_name": fields.String,
    "json_collection": fields.String(default="JsonCollection"),
    "generator": fields.String(default="DefaultLuceneDocumentGenerator"),
    "threads": fields.Integer(min=1, default=1)
})

dto_bm25_indexer_response = Model("DtoBM25IndexerResponse", {})

dto_sparse_indexer_request = Model("DtoSparseIndexerRequest", {
    "corpus_name": fields.String,
})

dto_sparse_indexer_response = Model("DtoSparseIndexerResponse", {})

dto_indexer_request = Model("DtoIndexerRequest", {
    "encode_type": fields.String(default="e.g., dense, traditional"),
    "model_name": fields.String(default="bert-base-german-cased"),
    "index_method": fields.String(default="e.g. flat-l2, flat-ip"),
    "dataset_name": fields.String(default="e.g. mls-tasks")
})

dto_indexer_response = Model("DtoIndexerResponse", {
    "message": fields.String()
})


## ------------- Encode Updater ---------------##
dto_index_updater = Model("DtoIndexUpdater", {
    "index_method": fields.String(),
    "language_model": fields.String(),
    "dataset": fields.String(),
    "state": fields.Integer(),
})

dto_index_updater_response = Model("DtoIndexUpdaterResponse", {
    "results": fields.List(fields.Nested(dto_index_updater))
})