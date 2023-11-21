import ast, os, pathlib
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string
import regex as re
# from pyserini.search.lucene import LuceneSearcher
# from pyserini.search.faiss import FaissSearcher, TctColBertQueryEncoder
import faiss


from l3s_search_srv.api.encoder.logic import BertGermanCasedDenseEncoder, XlmRobertaDenseEncoder

class Searcher(object):
    language_models = {
        "bert-base-german-cased": "dbmdz/bert-base-german-cased",
        "bert-base-german-uncased": "dbmdz/bert-base-german-cased"
    }
    punctuation_marks = string.punctuation.replace("-", "")
    
    def __init__(self):
        self.base_indexes_path = os.getenv("BASE_INDEXES_PATH")
    
    # def traditional_retrieval(self, query, index_name, dataset_name):
    #     index_path = os.path.join(self.base_indexes_path, f"{index_name}/{dataset_name}")
    #     searcher = LuceneSearcher(index_path)
    #     hits = searcher.search(query)
    #     results=[]
        
    #     if hits:
    #         for i in range(0, len(hits)):
    #             temp = ast.literal_eval(hits[i].raw)
    #             temp['score'] = f'{hits[i].score:.4f}'
    #             results.append(temp)
    #     return results
    
    
    def sparse_retrieval(self):
        pass
    
    
    def dense_retrieval(self, query, language_model, index_method, dataset_name):
        # remove the punctuations from the query
        # query = re.sub(r"\p{P}(?<!-)", "", query)
        query = query.translate(str.maketrans('', '', self.punctuation_marks))
        print(query)
        encodes_file_path = os.path.join(os.getenv("BASE_ENCODES_PATH"), f"dense/{language_model}/{dataset_name}/data_encoded.json")
        prebuilt_index_path = os.path.join(os.getenv("BASE_INDEXES_PATH"), f"{index_method}/{dataset_name}/dense/{language_model}/")
        
        print(encodes_file_path)
        print(prebuilt_index_path)
        
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

        # data = []
        with open(encodes_file_path, "r") as file:
            data = json.load(file)
            
        with open(f"{prebuilt_index_path}/docid", "r") as f:
            docid = f.read()
            
        D, I = index.search(xq, len(data))

        # transform distances and indexes to list
        distance = [round(n, 2) for n in D[0].tolist()]
        indexes = I[0].tolist()
        
        results = []
        for i in indexes:
            results.append(data[i])

        # add distance to results
        for i in range(len(data)):
            results[i]["distance"] = distance[i]
            # results[i]["ranking"] = i+1
            results[i]["jaccard"] = self.__jaccard(query, results[i]["contents"])
            results[i]["cosine_similarity"] = self.__cosine_sim(query_enc, results[i]["vector"])
            
                    
        # reranking the result
        rerank_category = ["jaccard", "cosine_similarity"]
        sorted_results = sorted(results, key=lambda x: x[rerank_category[1]], reverse=True)
        
        for item in sorted_results:
            item.pop("vector", None)
        
        return sorted_results
    
    
    def __cosine_sim(self, query, content):
        x = np.array(query).reshape(1, -1)
        y = np.array(content).reshape(1, -1)
        r = cosine_similarity(x, y)[0][0]
        return float("{:.4f}".format(r))
    
    def __jaccard(self, query, content):
        # if not type(x) == set or not type(y) == set:
        #     raise ValueError("input must be set.")
        
        # len(dataset.iloc[0]["task_text"].translate(str.maketrans('', '', string.punctuation)).split())
        query = query.lower()
        content = content.lower()
        
        x = set(query.translate(str.maketrans('', '', string.punctuation)).split())
        y = set(content.translate(str.maketrans('', '', string.punctuation)).split())

        n_shared = len(x.intersection(y))
        n_total = len(x.union(y))
        return float("{:.2f}".format(n_shared/len(x)))




