import os, subprocess
from transformers import XLMRobertaTokenizer, XLMRobertaModel
import torch

class SparseEncoder(object):
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

    
class DenseEncoder(object):
        
    def xlm_roberta_base(self, input_text):
        
        # Load the tokenizer and model
        tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
        model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
        tokens = tokenizer.encode(input_text, add_special_tokens=True, max_length=512)
        input_ids = torch.tensor([tokens])
        with torch.no_grad():
                outputs = model(input_ids)
                dense_vector = outputs[0][0][0]  # Extract the dense vector from the model output

        # Convert the dense vector to a numpy array
        dense_vector_list = dense_vector.numpy().tolist()

        # root = os.getenv("ROOT_PATH")
        
        # path_json_file = os.path.join(root, loc_json_file)
        
        # cmd = f"""
        #     python -m pyserini.encode \
        #     input   --corpus {path_json_file} \
        #             --fields text \
        #             --delimiter "\n" \
        #             --shard-id 0 \
        #             --shard-num 1 \
        #     output  --embeddings {path_output_dir} \
        #             --to-faiss \
        #     encoder --encoder castorini/tct_colbert-v2-hnp-msmarco \
        #             --fields text \
        #             --batch 32 \
        #             --fp16
        # """
        
        # p1 = subprocess.call(cmd, shell=True)
        return dense_vector_list