import os, subprocess


class Encoder(object):
    def sparse_encoder(path_json_file):
        cmd = f"""
            python -m pyserini.encode \
            input   --corpus {path_json_file} \
                    --fields text \
            output  --embeddings path/to/output/dir \
            encoder --encoder castorini/unicoil-d2q-msmarco-passage \
                    --fields text \
                    --batch 32 \
                    --fp16 # if inference with autocast()
        """
        pass
    
    
    def dense_encoder(self, path_json_file,
                      path_output_dir
                    ):
        
        root = os.getenv("ROOT_PATH")
        
        # path_json_file = os.path.join(root, loc_json_file)
        
        
        cmd = f"""
            python -m pyserini.encode \
            input   --corpus {path_json_file} \
                    --fields text \  # fields in collection contents
                    --delimiter "\n" \
                    --shard-id 0 \   # The id of current shard. Default is 0
                    --shard-num 1 \  # The total number of shards. Default is 1
            output  --embeddings {path_output_dir} \
                    --to-faiss \
            encoder --encoder castorini/tct_colbert-v2-hnp-msmarco \
                    --fields text \  # fields to encode, they must appear in the input.fields
                    --batch 32 \
                    --fp16
        """
        
        p1 = subprocess.call(cmd, shell=True)
        return p1