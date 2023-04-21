import subprocess, os

class Indexer(object):
    '''Indexer class'''
    
    def test(self):
        return {"Indexer": "Test funtion"}
    
    def bm25_indexer(
        self,
        dataset_name,
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
        dataset_jsonl_path = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{dataset_name}/jsonl")
        index_path = os.path.join(os.getenv("BASE_INDEXES_PATH"), f"bm25/{dataset_name}")

        print(dataset_jsonl_path)
        print(index_path)
        
        
        if not os.path.exists(dataset_jsonl_path): 
            raise NotADirectoryError("The dataset does not exist.")
        
        if not os.path.exists(index_path):
            os.makedirs(index_path)
        
        cmd = f"""
            python3 -m pyserini.index.lucene \
            --collection {json_collection} \
            --input {dataset_jsonl_path} \
            --index {index_path} \
            --generator  {generator} \
            --threads {threads} \
            --storePositions \
            --storeDocvectors \
            --storeRaw \
        """
        
        # dataset_path = f"./datasets/{corpus_name}"
        
        
        p1 = subprocess.call(cmd, shell=True)
        
        return 1
        
    
    
    
    
    def hnswpq_indexer(self):
        cmd = """
            python -m pyserini.index.faiss \
                --input path/to/encoded/corpus \  # either in the Faiss or the jsonl format
                --output path/to/output/index \
                --hnsw \
                --pq
        """
        pass
    
    
    def hnsw_indexer(self, encode_cat, model_name, dataset_name):
        dataset_encode_path = os.path.join(os.getenv("BASE_ENCODES_PATH"),
                                            f"{encode_cat}/{model_name}/{dataset_name}"
                                        )
        if not os.path.exists(dataset_encode_path):
            raise FileNotFoundError
        
        output_path = os.path.join(os.getenv("BASE_INDEXES_PATH"), f"{encode_cat}/hnsw/{dataset_name}")
        # print(output_path)
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        hnsw_cmd = f"""
            python -m pyserini.index.faiss \
                --input {dataset_encode_path} \
                --output {output_path} \
                --hnsw
        """
        
        subprocess.call(hnsw_cmd, shell=True)
        return 1
    
    
    def pq_indexer(self, encode_cat, model_name, dataset_name):
        dataset_encode_path = os.path.join(os.getenv("BASE_ENCODES_PATH"),
                                            f"{encode_cat}/{model_name}/{dataset_name}"
                                        )
        if not os.path.exists(dataset_encode_path):
            raise FileNotFoundError
        
        output_path = os.path.join(os.getenv("BASE_INDEXES_PATH"), f"{encode_cat}/pq/{dataset_name}")
        # print(output_path)
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
        pq_cmd = f"""
            python -m pyserini.index.faiss \
                --input {dataset_encode_path} \
                --output {output_path} \
                --pq
        """
        subprocess.call(pq_cmd, shell=True)
        return 1
    
    
    def flat_indexer():
        cmd = """
            python -m pyserini.index.faiss \
                --input path/to/encoded/corpus \  # in jsonl format
                --output path/to/output/index \
        """
        pass
    