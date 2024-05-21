import subprocess, os
import json
import numpy as np
import faiss
from rank_bm25 import BM25Okapi

from l3s_search_srv.util.meta import get_subdirs


class Indexer(object):
    '''Indexer class'''
    
    FLAT_INDEX_METHOD = ["flat-ip", "flat-l2"]
    
    ## ---------- private methods ------------- ##
    def __add_new_doc(document, dataset_name):
        json_file_path = os.path.join(os.getenv("BASE_DATASETS_DIR"), dataset_name+"/data.json")
        try:
            with open(json_file_path, "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = {}
        
        if type(document) is dict:
            new_element = {
                "id": document["id"],
                "contents": document["contents"],
                "@id": document["@id"]
            }
            
        return 1
    
    ## ------------- public methods-------------- ##
    def test(self):
        return {"Indexer": "Test funtion"}
    
    
    ## ------------- bm25 -------------- ##
    # def bm25_indexer(
    #     self,
    #     dataset_name,
    #     json_collection="JsonCollection",
    #     generator="DefaultLuceneDocumentGenerator",
    #     threads=1,
    #     ):
    #     # cmd = f"""
    #     #     python3 -m pyserini.index.lucene \
    #     #     --collection JsonCollection \
    #     #     --input ./datasets/{corpus_name} \
    #     #     --index ./indexes/{corpus_name} \
    #     #     --generator DefaultLuceneDocumentGenerator \
    #     #     --threads 1 \
    #     #     --storePositions --storeDocvectors --storeRaw
    #     # """
    #     dataset_jsonl_path = os.path.join(os.getenv("BASE_DATASETS_DIR"), f"{dataset_name}/jsonl")
    #     index_path = os.path.join(os.getenv("BASE_INDEXES_DIR"), f"bm25/{dataset_name}")

    #     print(dataset_jsonl_path)
    #     print(index_path)
        
        
    #     if not os.path.exists(dataset_jsonl_path): 
    #         raise NotADirectoryError("The dataset does not exist.")
        
    #     if not os.path.exists(index_path):
    #         os.makedirs(index_path)
        
    #     cmd = f"""
    #         python3 -m pyserini.index.lucene \
    #         --collection {json_collection} \
    #         --input {dataset_jsonl_path} \
    #         --index {index_path} \
    #         --generator  {generator} \
    #         --threads {threads} \
    #         --storePositions \
    #         --storeDocvectors \
    #         --storeRaw \
    #     """
        
    #     # dataset_path = f"./datasets/{corpus_name}"
        
        
    #     p1 = subprocess.call(cmd, shell=True)
        
    #     return 1
        
    
    
    def flat(self, encode_type, model_name, index_method, dataset_name):
        print("supported index methods: ", self.FLAT_INDEX_METHOD)
        # check if index method is valid
        
        datasets = get_subdirs(os.getenv('BASE_DATASETS_DIR'))
        # print(datasets)
        if dataset_name not in datasets:
            raise ValueError("Invalid dataset!")
        
        if encode_type != "dense":
            raise ValueError("Invalid encode type, try 'dense' instead!")
        
        if index_method not in self.FLAT_INDEX_METHOD:
            raise ValueError("Invalid index method, try 'flat-ip' or 'flat-l2' instead!")
        
        
        input_encode_path = os.path.join(os.getenv("BASE_ENCODES_DIR"), f"{encode_type}/{model_name}/{dataset_name}/data_encoded.json")
        output_index_path = os.path.join(os.getenv("BASE_INDEXES_DIR"), f"{index_method}/{dataset_name}/{encode_type}/{model_name}/")
        
        if not os.path.exists(input_encode_path):
            # print(input_path)
            raise FileNotFoundError
        
        if not os.path.exists(output_index_path):
            os.makedirs(output_index_path)
        
        # print(input_encode_path)
        # print(output_index_path)
        docid = []
        temp = []
        
        # load file and fetch the encodings
        with open(input_encode_path) as file:
            data_json = json.load(file)
            # print(len(data_json))
            for d in data_json:
                temp.append(d["vector"])
                docid.append(d["entity_id"])

        embeddings = np.float32(np.array(temp))
        dim = embeddings.shape[1]   # dimension of input
        
        if index_method == "flat-l2":
            index = faiss.IndexFlatL2(dim)
        elif index_method == "flat-ip":
            index = faiss.IndexFlatIP(dim)
        
        if index.is_trained:
            index.add(embeddings)
        
        # save file as index.faiss
        faiss.write_index(index, f"{output_index_path}/index.faiss")
        
        # save the docid
        with open(f"{output_index_path}/docid", "w") as output:
            output.write(str(docid))
        
        return 1
    
    
    def flat_update(document, dataset_name, encode_type, model_name, index_method):
        # add the new document to the dataset
        
        index = faiss.read_index()
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
        dataset_encode_path = os.path.join(os.getenv("BASE_ENCODES_DIR"),
                                            f"{encode_cat}/{model_name}/{dataset_name}"
                                        )
        if not os.path.exists(dataset_encode_path):
            raise FileNotFoundError
        
        output_path = os.path.join(os.getenv("BASE_INDEXES_DIR"), f"{encode_cat}/hnsw/{dataset_name}")
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
        dataset_encode_path = os.path.join(os.getenv("BASE_ENCODES_DIR"),
                                            f"{encode_cat}/{model_name}/{dataset_name}"
                                        )
        if not os.path.exists(dataset_encode_path):
            raise FileNotFoundError
        
        output_path = os.path.join(os.getenv("BASE_INDEXES_DIR"), f"{encode_cat}/pq/{dataset_name}")
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
    
    # def flat_ip(self, encoding_type, model_name, dataset_name):
        
        
    #     input_path = os.path.join(os.getenv("BASE_ENCODES_DIR"), f"{encoding_type}/{model_name}/{dataset_name}/data_encoded.jsonl")
    #     output_path = os.path.join(os.getenv("BASE_INDEXES_DIR"), f"{encoding_type}/{model_name}/flat/{dataset_name}")
        
    #     if not os.path.exists(input_path):
    #         raise FileNotFoundError
        
    #     if not os.path.exists(output_path):
    #         os.makedirs(output_path)
            
    #     # p = subprocess.call(cmd, shell=True)
    #     docid = []
    #     temp = []
    #     # load file and fetch the encodings
    #     with open(input_path) as data:
    #         for line in data:
    #             json_obj = json.loads(line)
    #             temp.append(json_obj["vector"])
    #             docid.append(json_obj["id"])

    #     embeddings = np.float32(np.array(temp))
    #     dim = embeddings.shape[1]   # dimension of input
    #     index = faiss.IndexFlatIP(dim)
        
    #     if index.is_trained:
    #         index.add(embeddings)
        
    #     # save file as index.faiss
    #     faiss.write_index(index, f"{output_path}/index.faiss")
        
    #     # save the docid
    #     with open(f"{output_path}/docid", "w") as output:
    #         output.write(str(docid))
        
    #     return
    