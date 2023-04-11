import ast, os, pathlib
from pyserini.search.lucene import LuceneSearcher


class SimpleSearcher(object):
    def __init__(self, base_path_index):
        self.base_path_index = base_path_index
    
    def get_hits(self, query, dataset_name):
        # print(os.path.join(pathlib.Path(__name__).parent.absolute(), 'datasets/scidocs/index'))
        # searcher = LuceneSearcher(os.path.join(pathlib.Path(__name__).parent.absolute(), 'indexes/scidocs'))
        # print(f'base: {self.base_path_index}')
        path_index = os.path.join(self.base_path_index, dataset_name)
        # print(path_index)
        searcher = LuceneSearcher(path_index)
        hits = searcher.search(query)
        
        return hits
    
    def sparse_retrieval(self, query, dataset_name):
        # form = SearchForm()
        results=[]
        # if form.validate_on_submit:
        #     if request.method == 'POST':
        #         # results = retriever.retrieve(corpus, form.query)
        hits = self.get_hits(query, dataset_name)
        if hits:
            for i in range(0, len(hits)):
                temp = ast.literal_eval(hits[i].raw)
                temp['score'] = f'{hits[i].score:.4f}'
                results.append(temp)
                
        # return render_template('search.html', title='Search', form=form, results=results)
        return results