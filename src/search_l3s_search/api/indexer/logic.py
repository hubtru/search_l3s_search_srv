import subprocess, os

class Indexer(object):
    '''Indexer class'''
    
    def test(self):
        return {"Indexer": "Test funtion"}
    
    def bm25_indexer(
        self,
        corpus_name,
        json_collection="JsonCollection",
        generator="DefaultLuceneDocumentGenerator",
        threads=1,
        ):
        # cmd = f"""
        #     python3 -m pyserini.index.lucene \
        #     --collection JsonCollection \
        #     --input ./datasets/{corpus_name} \
        #     --index ./indexes/{corpus_name} \
        #     --generator DefaultLuceneDocumentGenerator \
        #     --threads 1 \
        #     --storePositions --storeDocvectors --storeRaw
        # """
        dataset_path = f"./datasets/{corpus_name}"
        index_path = f"./indexes/bm25/{corpus_name}"
        # print(dataset_path)
        # print(index_path)
        
        if not os.path.isdir(dataset_path): 
            raise NotADirectoryError("The dataset does not exist.")
        
        cmd = f"""
            python3 -m pyserini.index.lucene \
            --collection {json_collection} \
            --input {dataset_path} \
            --index {index_path} \
            --generator  {generator} \
            --threads {threads} \
            --storePositions \
            --storeDocvectors \
            --storeRaw \
        """
        
        # dataset_path = f"./datasets/{corpus_name}"
        
        
        p1 = subprocess.call(cmd, shell=True)
        
    
    
    
    
    def hnswpq_indexer():
        cmd = """
            python -m pyserini.index.faiss \
                --input path/to/encoded/corpus \  # either in the Faiss or the jsonl format
                --output path/to/output/index \
                --hnsw \
                --pq
        """
        pass
    
    
    def hnsw_indexer():
        cmd = """
            python -m pyserini.index.faiss \
                --input path/to/encoded/corpus \  # either in the Faiss or the jsonl format
                --output path/to/output/index \
                --hnsw
        """
        pass
    
    
    def pq_indexer():
        cmd = """
            python -m pyserini.index.faiss \
                --input path/to/encoded/corpus \  # either in the Faiss or the jsonl format
                --output path/to/output/index \
                --pq
        """
        pass
    
    
    def flat_indexer():
        cmd = """
            python -m pyserini.index.faiss \
                --input path/to/encoded/corpus \  # in jsonl format
                --output path/to/output/index \
        """
        pass