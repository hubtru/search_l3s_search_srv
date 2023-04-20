import ast, os, pathlib
from pyserini.search.lucene import LuceneSearcher
from pyserini.search.faiss import FaissSearcher, TctColBertQueryEncoder

# from search_l3s_search.api.encoder.logic import DenseEncoder

class Searcher(object):
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
    
    
    def dense_retrieval(self, query, index_method, dataset_name):
        # encoder = DenseEncoder()
        # encoder = TctColBertQueryEncoder('castorini/tct_colbert-msmarco')
        prebuilt_index_path = os.path.join(self.base_indexes_path, f"dense/{index_method}/{dataset_name}")
        print(prebuilt_index_path)
        search_engine = FaissSearcher(
            prebuilt_index_path,
            "xlm-roberta-base"
        )
        
        print(search_engine)
        
        hits = search_engine.search(query)
        results=[]
        
        # if hits:
        #     for i in range(0, len(hits)):
        #         temp = ast.literal_eval(hits[i].raw)
        #         temp['score'] = f'{hits[i].score:.4f}'
        #         results.append(temp)
        
        for i in range(0, 10):
            
            print(f'{i+1:2} {hits[i].docid:7} {hits[i].score:.5f}')
            
        return results
    
