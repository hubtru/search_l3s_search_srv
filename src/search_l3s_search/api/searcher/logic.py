import ast, os, pathlib
from pyserini.search.lucene import LuceneSearcher


class Searcher(object):
    def __init__(self, base_path_index):
        self.base_path_index = base_path_index
    
    def traditional_retrieval(self, query, index_name, dataset_name):
        p = index_name + '/' + dataset_name
        path_index = os.path.join(self.base_path_index, p)
        searcher = LuceneSearcher(path_index)
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
    
    
    def dense_retrieval(self):
        pass
    
