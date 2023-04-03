import subprocess, os

class Indexer(object):
    '''Indexer class'''
    
    def test(self):
        return {"Indexer": "Test funtion"}
    
    def pyserini_indexer(self, corpus_name):
        cmd = f"""
                python3 -m pyserini.index.lucene \
            --collection JsonCollection \
            --input ./datasets/{corpus_name} \
            --index ./indexes/{corpus_name} \
            --generator DefaultLuceneDocumentGenerator \
            --threads 1 \
            --storePositions --storeDocvectors --storeRaw
        """
        
        dataset_path = f"./datasets/{corpus_name}"
        if not os.path.isdir(dataset_path): 
            raise NotADirectoryError("The dataset does not exist.")
        
        p1 = subprocess.call(cmd, shell=True)