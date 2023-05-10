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

indexer_input_model = Model("IndexerInput", {
    "encode_type": fields.String(default="e.g., dense, traditional"),
    "model_name": fields.String(default="bert_german_uncased"),
    "index_method": fields.String(default="e.g. flat_l2, flat_ip, flat_pq, flat_hnsw"),
    "dataset_name": fields.String(default="e.g. mls-tasks")
})