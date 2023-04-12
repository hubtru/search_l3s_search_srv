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
        
    
    def sparse_encoder():
        cmd = """
            python -m pyserini.encode \
            input   --corpus tests/resources/simple_cacm_corpus.json \
                    --fields text \
            output  --embeddings path/to/output/dir \
            encoder --encoder castorini/unicoil-d2q-msmarco-passage \
                    --fields text \
                    --batch 32 \
                    --fp16 # if inference with autocast()
        """
        pass
    
    
    def dense_encoder():
        cmd = """
            python -m pyserini.encode \
            input   --corpus tests/resources/simple_cacm_corpus.json \
                    --fields text \  # fields in collection contents
                    --delimiter "\n" \
                    --shard-id 0 \   # The id of current shard. Default is 0
                    --shard-num 1 \  # The total number of shards. Default is 1
            output  --embeddings path/to/output/dir \
                    --to-faiss \
            encoder --encoder castorini/tct_colbert-v2-hnp-msmarco \
                    --fields text \  # fields to encode, they must appear in the input.fields
                    --batch 32 \
                    --fp16  # if inference with autocast()
        """
        pass
    
    
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