import ast, os, pathlib
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from pyserini.search.lucene import LuceneSearcher
# from pyserini.search.faiss import FaissSearcher, TctColBertQueryEncoder
import faiss


from search_l3s_search.api.encoder.logic import BertGermanCasedDenseEncoder, XlmRobertaDenseEncoder

class Searcher(object):
    language_models = {
        "bert-base-german-uncased": "dbmdz/bert-base-german-cased"
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
        
        encodes_file_path = os.path.join(os.getenv("BASE_ENCODES_PATH"), f"dense/{language_model}/{dataset_name}/data_encoded.jsonl")
        prebuilt_index_path = os.path.join(os.getenv("BASE_INDEXES_PATH"), f"dense/{language_model}/{index_method}/{dataset_name}")
        
        if language_model not in ["bert-base-german-cased", "xlm-roberta-base"]:
            raise ValueError("language model not defined")
        
        if index_method not in ["flat-l2", "flat-ip", "hnsw", "pq"]:
            raise ValueError("index method not defined")

        # load index
        if not os.path.exists(prebuilt_index_path):
            print(prebuilt_index_path)
            raise ValueError("index path not exists")
        
        index = faiss.read_index(os.path.join(prebuilt_index_path, "index.faiss"))
        if language_model == "bert-base-german-cased":
            encoder = BertGermanCasedDenseEncoder()
        elif language_model == "xlm-roberta-base":
            encoder = XlmRobertaDenseEncoder()
        else:
            raise ValueError("search with the given language model is not implemented") 

        query_enc = encoder.query_encoder(query)
        
        xq = np.float32(np.array([query_enc]))

        D, I = index.search(xq, num_results)
        print(D)
        print(I)
        # transform distances and indexes to list
        distance = [round(n, 2) for n in D[0].tolist()]
        indexes = I[0].tolist()
        
        data = []
        with open(encodes_file_path, "r") as f:
            data_list = list(f)
            for d in data_list:
                data.append(json.loads(d))
            
        with open(f"{prebuilt_index_path}/docid", "r") as f:
            docid = f.read()
        
        results = []
        for i in indexes:
            results.append(data[i])

        # add distance to results
        for i in range(int(num_results)):
            results[i]["distance"] = distance[i]
            results[i]["ranking"] = i+1
            results[i]["jaccard"] = self.__jac(query, results[i]["contents"])
            results[i]["cosine_similarity"] = self.__cosine_sim(query_enc, results[i]["vector"])
            
                    
        # reranking the result
        sorted_results = sorted(results, key=lambda x: x["jaccard"], reverse=True)
        
        for item in sorted_results:
            item.pop("vector", None)
        
        return sorted_results
    
    
    def __cosine_sim(self, query, content):
        x = np.array(query).reshape(1, -1)
        y = np.array(content).reshape(1, -1)
        r = cosine_similarity(x, y)[0][0]
        return float("{:.4f}".format(r))
    
    def __jac(self, query, content):
        # if not type(x) == set or not type(y) == set:
        #     raise ValueError("input must be set.")
        x = set(query.split())
        y = set(content.split())
        n_shared = len(x.intersection(y))
        n_total = len(x.union(y))
        return float("{:.2f}".format(n_shared/n_total))
