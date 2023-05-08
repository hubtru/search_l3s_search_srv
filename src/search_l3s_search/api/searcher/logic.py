import ast, os, pathlib
import json
import numpy as np

from pyserini.search.lucene import LuceneSearcher
# from pyserini.search.faiss import FaissSearcher, TctColBertQueryEncoder
import faiss


from search_l3s_search.api.encoder.logic import BertGermanUncasedDenseEncoder

class Searcher(object):
    language_models = {
        "bert_german_uncased": "dbmdz/bert-base-german-cased"
    }
    
    def __init__(self, base_path_index):
        self.base_indexes_path = base_path_index
    
    def traditional_retrieval(self, query, index_name, dataset_name):
        index_path = os.path.join(self.base_indexes_path, f"{index_name}/{dataset_name}")
        searcher = LuceneSearcher(index_path)
        hits = searcher.search(query)
        results=[]
        
        if hits:
            for i in range(0, len(hits)):
                temp = ast.literal_eval(hits[i].raw)
                temp['score'] = f'{hits[i].score:.4f}'
                results.append(temp)
        return results
    
    
    def sparse_retrieval(self):
        pass
    
    
    def dense_retrieval(self, query, language_model, index_method, dataset_name, num_results):
        
        dataset_file_path = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{dataset_name}/json/data.json")
        prebuilt_index_path = os.path.join(os.getenv("BASE_INDEXES_PATH"), f"dense/{language_model}/{index_method}/{dataset_name}")
        
        # load index
        if not os.path.exists(prebuilt_index_path):
            raise ValueError
        
        index = faiss.read_index(os.path.join(prebuilt_index_path, "index.faiss"))
        if language_model == "bert-german-uncased":
            encoder = BertGermanUncasedDenseEncoder()
        else:
            raise ValueError("search with the given language model is not implemented") 

        query_enc = encoder.query_encoder(query)
        
        xq = np.float32(np.array([query_enc]))

        # transform distances and indexes to list
        D, I = index.search(xq, num_results)
        distance = [round(n, 2) for n in D[0].tolist()]
        indexes = I[0].tolist()
        
        
        with open(dataset_file_path, "r") as f:
            data = json.load(f)

        with open(f"{prebuilt_index_path}/docid", "r") as f:
            docid = f.read()
        
        results = [data[i] for i in indexes]
        
        # add distance to results
        for i in range(int(num_results)):
            results[i]["distance"] = distance[i]
        
        return results
    
