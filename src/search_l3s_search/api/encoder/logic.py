import os, subprocess, json
from http import HTTPStatus
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
        
        def xlm_roberta_query_encoder(self, input_text):
                # Load the tokenizer and model
                # tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
                # model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
                tokens = self.tokenizer.encode(input_text, add_special_tokens=True, max_length=512, truncation=True)
                input_ids = torch.tensor([tokens])
                with torch.no_grad():
                        outputs = self.model(input_ids)
                        dense_vector = outputs[0][0][0]  # Extract the dense vector from the model output

                # Convert the dense vector to a numpy array
                dense_vector_list = dense_vector.numpy().tolist()
                return dense_vector_list

        
        def xlm_roberta_dataset_encoder(self, dataset_name):
                # tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
                # model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
                # tokens = self.tokenizer.encode(input_text, add_special_tokens=True, max_length=512, truncation=True)
                model_name = "xlm_roberta_base"
                
                input_file_dir = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{dataset_name}/jsonl/data.jsonl")
                
                output_dir = os.path.join(os.getenv("BASE_ENCODES_PATH"), f"dense_encoder/{model_name}/{dataset_name}")
                
                
                if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                        
                print(output_dir)
                
                try:
                        with open(input_file_dir) as input_file:
                                for line in input_file:
                                        json_obj = json.loads(line)
                                        json_obj["vector"] = self.xlm_roberta_query_encoder(json_obj["contents"])
                                        # print(json_obj)
                                        
                                        with open(f"{output_dir}/data_encoded.jsonl", "w") as jsonl_file:
                                                json.dump(json_obj, jsonl_file)
                                                jsonl_file.write('\n')
                except FileNotFoundError:
                        return HTTPStatus.NOT_FOUND
                        
                return 1

