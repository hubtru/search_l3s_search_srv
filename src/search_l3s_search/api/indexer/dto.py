from flask_restx import Model, fields
# from search_l3s_search.api.indexer import ns_indexer

corpus_model = Model("Corpus", {
    "name": fields.String()
})

document_model = Model("Document", {
    "id": fields.String,
    "content": fields.String,
})

request_mls_index_update_model = Model("MlsIndexUpdate", {
    "datasets": fields.List(fields.String),
})

bm25_indexer_input_model = Model("BM25Indexer", {
    "dataset_name": fields.String,
    "json_collection": fields.String(default="JsonCollection"),
    "generator": fields.String(default="DefaultLuceneDocumentGenerator"),
    "threads": fields.Integer(min=1, default=1)
})

SPARSE_INDEX_model = Model("SparseIndex", {
    "corpus_name": fields.String,
})

dense_indexer_input_model = Model("HNSW_Index", {
    "encode_cat": fields.String,
    "model_name": fields.String,
    "dataset_name": fields.String
})