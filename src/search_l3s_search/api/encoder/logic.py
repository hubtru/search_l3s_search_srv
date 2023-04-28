import os, subprocess, json
from http import HTTPStatus
from transformers import XLMRobertaTokenizer, XLMRobertaModel
from transformers import AutoModel, AutoTokenizer, AutoModelWithLMHead
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



class DenseEncoer(object):
	def __init__(self) -> None:
		self.tokenizer = None
		self.model = None
		self.model_name = None
                
	def print_model_name(self):
		print(self.model_name)
		return


	def query_encoder(self, input_text):
		# tokens = self.tokenizer.encode(input_text, add_special_tokens=True, max_length=512, truncation=True)
		tokens = self.tokenizer.encode(input_text, add_special_tokens=True, max_length=512)
		input_ids = torch.tensor([tokens])
		with torch.no_grad():
			outputs = self.model(input_ids)
			dense_vector = outputs[0][0][0]  # Extract the dense vector from the model output

		# Convert the dense vector to a numpy array
		dense_vector_list = dense_vector.numpy().tolist()
		return dense_vector_list

        
	def dataset_encoder(self, dataset_name):                
		# input_file_path = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{dataset_name}/jsonl/data.jsonl")
		# output_dir_path = os.path.join(os.getenv("BASE_ENCODES_PATH"), f"dense/{self.model_name}/{dataset_name}")
  
		input_file_path = os.path.join(os.getcwd(), f"datasets/{dataset_name}/jsonl/data.jsonl")
		output_dir_path = os.path.join(os.getcwd(), f"encodes/dense/{self.model_name}/{dataset_name}")
  
		# print(input_file_path)
		# print(output_dir_path)
                
		if not os.path.exists(output_dir_path):
				os.makedirs(output_dir_path)
                        
		output_file_path = os.path.join(output_dir_path, "data_encoded.jsonl")
                                        
		try:
			with open(input_file_path) as input_file:
				for line in input_file:
					json_obj = json.loads(line)
					json_obj["vector"] = self.query_encoder(json_obj["contents"])
					# print(json_obj)
						
					with open(output_file_path, "a") as jsonl_file:
						json.dump(json_obj, jsonl_file)
						jsonl_file.write('\n')
      
		except FileNotFoundError:
				return HTTPStatus.NOT_FOUND
		return 1


class GermanGPT2DenseEncoder(DenseEncoer):
    def __init__(self) -> None:
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained("dbmdz/german-gpt2-faust")
        self.model = AutoModelWithLMHead.from_pretrained("dbmdz/german-gpt2-faust")
        self.model_name = "german_chatgpt_2"


class BertGermanUncasedDenseEncoder(DenseEncoer):
	def __init__(self) -> None:
		super().__init__()
		self.tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-german-cased")
		self.model = AutoModel.from_pretrained("dbmdz/bert-base-german-cased")
		self.model_name = "bert_german_uncased"


class XlmRobertaDenseEncoder(DenseEncoer):
	def __init__(self) -> None:
		super().__init__()
		self.tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
		self.model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
		self.model_name = "xlm_roberta_model"
                
        
        
        # def xlm_roberta_query_encoder(self, input_text):
        #         tokens = self.tokenizer.encode(input_text,
        #                                        add_special_tokens=True,
        #                                        max_length=512,
        #                                        truncation=True
        #                                 )
        #         input_ids = torch.tensor([tokens])
        #         with torch.no_grad():
        #                 outputs = self.model(input_ids)
        #                 dense_vector = outputs[0][0][0]  # Extract the dense vector from the model output

        #         # Convert the dense vector to a numpy array
        #         dense_vector_list = dense_vector.numpy().tolist()
        #         return dense_vector_list

        
        # def xlm_roberta_dataset_encoder(self, dataset_name):                
        #         input_file_path = os.path.join(os.getenv("BASE_DATASETS_PATH"), f"{dataset_name}/jsonl/data.jsonl")
                
        #         output_dir_path = os.path.join(os.getenv("BASE_ENCODES_PATH"), f"dense/xlm-roberta-base/{dataset_name}")
                
                
        #         if not os.path.exists(output_dir_path):
        #                 os.makedirs(output_dir_path)
                        
        #         output_file_path = os.path.join(output_dir_path, "data_encoded.jsonl")
                                        
        #         try:
        #                 with open(input_file_path) as input_file:
        #                         for line in input_file:
        #                                 json_obj = json.loads(line)
        #                                 json_obj["vector"] = self.xlm_roberta_query_encoder(json_obj["contents"])
        #                                 # print(json_obj)
                                        
        #                                 with open(output_file_path, "a") as jsonl_file:
        #                                         json.dump(json_obj, jsonl_file)
        #                                         jsonl_file.write('\n')
        #         except FileNotFoundError:
        #                 return HTTPStatus.NOT_FOUND
                        
        #         return 1

