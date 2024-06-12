import os, json
# import subprocess
# from http import HTTPStatus
# from transformers import XLMRobertaTokenizer, XLMRobertaModel
from transformers import AutoModel, AutoTokenizer
import torch
import string


# class SparseEncoder(object):
# 	def sparse_encoder(path_json_file):
# 		cmd = f"""
# 		python -m pyserini.encode \
# 		input   --corpus {path_json_file} \
# 				--fields text \
# 		output  --embeddings path/to/output/dir \
# 		encoder --encoder castorini/unicoil-d2q-msmarco-passage \
# 				--fields text \
# 				--batch 32 \
# 				--fp16 # if inference with autocast()
# 		"""
# 		pass


class DenseEncoer(object):
    def __init__(self) -> None:
        self.tokenizer = None
        self.model = None
        self.model_name = None
        self.punctuation_marks = string.punctuation.replace("-", "")

    def print_model_name(self):
        print(self.model_name)
        return

    def query_encoder(self, input_text):
        # tokens = self.tokenizer.encode(input_text, add_special_tokens=True, max_length=512, truncation=True)
        tokens = self.tokenizer(input_text,
                                #  add_special_tokens=True,
                                #  padding='max_length',
                                padding=False,
                                max_length=512,
                                truncation=True,
                                return_tensors='pt'
                                )

        input_ids = tokens.get('input_ids')
        outputs = self.model(input_ids)
        embeddings = outputs.last_hidden_state
        masks = tokens.get('attention_mask').unsqueeze(-1).expand(embeddings.size()).float()
        masked_embeddings = embeddings * masks
        summed = torch.sum(masked_embeddings, 1)
        counted = torch.clamp(masks.sum(1), min=1e-9)
        mean_pooled = summed / counted
        # Convert the dense vector to a numpy array
        dense_vector_list = mean_pooled.tolist()[0]
        # print(len(dense_vector_list))
        return dense_vector_list

    def dataset_encoder(self, dataset_name):
        input_file_path = os.path.join(os.getenv("BASE_DATASETS_DIR"), f"{dataset_name}/data.json")
        output_dir_path = os.path.join(os.getenv("BASE_ENCODES_DIR"), f"dense/{self.model_name}/{dataset_name}")

        # input_file_path = os.path.join(os.getcwd(), f"datasets/{dataset_name}/json/data.json")
        # output_dir_path = os.path.join(os.getcwd(), f"encodes/dense/{self.model_name}/{dataset_name}")

        if not os.path.exists(input_file_path):
            raise ValueError("input file does not exist")

        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)

        output_file_path = os.path.join(output_dir_path, "data_encoded.json")

        with open(input_file_path) as input_file:
            data = json.load(input_file)

        i = 1
        l = len(data)
        encoded_data = []
        for d in data:
            d["preprocessed_contents"] = d["contents"].translate(str.maketrans('', '', self.punctuation_marks))
            d["vector"] = self.query_encoder(d["preprocessed_contents"])
            encoded_data.append(d)
            print(f"Progress: {(i / l) * 100:.2f}%")
            i += 1

        with open(output_file_path, "w") as json_file:
            json.dump(encoded_data, json_file)
            json_file.write('\n')

        # tokens = self.tokenizer(
        # 					contents,
        #                     add_special_tokens=True,
        #                     padding='max_length',
        #                     max_length=512,
        #                     truncation=True,
        #                     return_tensors='pt'
        #                 )

        # print(tokens.keys())
        # print(tokens.input_ids.shape)

        # for i in range(len(tokens.input_ids)):
        # 	print(i)
        # 	with torch.no_grad():
        # 		input_ids = tokens.input_ids[i].unsqueeze(-1)
        # 		outputs = self.model(input_ids)
        # 		print(outputs.last_hidden_state.shape)

        # print(outputs.shape)

        # outputs = self.model(**tokens)

        # embeddings = outputs.last_hidden_state

        # print(f"embeddings: {embeddings.shape}")

        # masks = tokens['attention_mask'].unsqueeze(-1).expand(embeddings.size()).float()
        # # print(masks)
        # print(f"mask: {masks.shape}")

        # masked_embeddings = embeddings * masks
        # print(f"masked embeddings: {masked_embeddings.shape}")

        # summed = torch.sum(masked_embeddings, 1)
        # print(f"summed: {summed.shape}")

        # counted = torch.clamp(masks.sum(1), min=1e-9)
        # print(f"counted: {counted.shape}")

        # mean_pooled = summed / counted

        # # print(mean_pooled)
        # print(f"mean_pooled: {mean_pooled.shape}")

        # print(mean_pooled[0].tolist())

        # for i in range(len(data)):
        # 	data[i]["vector"] = mean_pooled[i].tolist()

        # print(data)

        # with open(output_file_path, "w") as jsonl_file:
        # 	json.dump(data, jsonl_file)
        # 	jsonl_file.write('\n')

        # try:
        # 	with open(input_file_path) as input_file:
        # 		for line in input_file:
        # 			json_obj = json.loads(line)
        # 			json_obj["vector"] = self.query_encoder(json_obj["contents"])
        # 			# print(json_obj)

        # 			with open(output_file_path, "a") as jsonl_file:
        # 				json.dump(json_obj, jsonl_file)
        # 				jsonl_file.write('\n')

        # except FileNotFoundError:
        # 		return HTTPStatus.NOT_FOUND
        return 1

    def __sbert_embedding():
        pass


class CrossRobertaSentenceTransformerEncoder(DenseEncoer):
    def __init__(self) -> None:
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained("T-Systems-onsite/cross-en-de-roberta-sentence-transformer")
        self.model = AutoModel.from_pretrained("T-Systems-onsite/cross-en-de-roberta-sentence-transformer")
        self.model_name = "cross-en-de-roberta-sentence-transformer"


class BertGermanCasedDenseEncoder(DenseEncoer):
    def __init__(self) -> None:
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-german-cased")
        self.model = AutoModel.from_pretrained("dbmdz/bert-base-german-cased")
        self.model_name = "bert-base-german-cased"

# class XlmRobertaDenseEncoder(DenseEncoer):
#     def __init__(self) -> None:
#        super().__init__()
#        self.tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
#        self.model = XLMRobertaModel.from_pretrained("xlm-roberta-base")
#        self.model_name = "xlm-roberta-base"

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
    #         input_file_path = os.path.join(os.getenv("BASE_DATASETS_DIR"), f"{dataset_name}/jsonl/data.jsonl")

    #         output_dir_path = os.path.join(os.getenv("BASE_ENCODES_DIR"), f"dense/xlm-roberta-base/{dataset_name}")

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
