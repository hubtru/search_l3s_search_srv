import os, subprocess, json
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
        
        def __init__(self):
                self.tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
                self.model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
        
        def xlm_roberta_base_encoder(self, input_text):
                # Load the tokenizer and model
                # tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
                # model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
                tokens = self.tokenizer.encode(input_text, add_special_tokens=True, max_length=512, pad_to_max_length=True, return_tensors='pt')
                input_ids = torch.tensor([tokens])
                with torch.no_grad():
                        outputs = self.model(input_ids)
                        dense_vector = outputs[0][0][0]  # Extract the dense vector from the model output

                # Convert the dense vector to a numpy array
                dense_vector_list = dense_vector.numpy().tolist()
                return dense_vector_list

        
        def document_encoder(self):
                # tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
                # model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
                tokens = self.tokenizer.encode(input_text, add_special_tokens=True, max_length=512, pad_to_max_length=True, return_tensors='pt')
                
                input_file = os.path.join(os.getenv("ROOT_PATH"), "datasets/mls-tasks/tasks.json")
                output_file = os.path.join(os.getenv("ROOT_PATH"), "encodes/dense_encoder")
                
                with open(input_file) as f:
                        data = json.load(f)


                for d in data:
                        d["@id"] = d["id"]
                        d["id"] = int(d["id"].split("/")[-1])
                        d["vector"] = self.xlm_roberta_base_encoder(d["contents"]).tolist()

                        with open("encodes/dense_encoder/tasks.jsonl", "w") as jsonl_file:
                                for d in data:
                                        json.dump(d, jsonl_file)
                                        jsonl_file.write('\n')


