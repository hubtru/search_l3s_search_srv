import os, requests
from transformers import AutoModel, AutoTokenizer

## download the pre-trained models
models = ["dbmdz/bert-base-german-cased",
          "xlm-roberta-base",
          "dbmdz/german-gpt2-faust",
          "ikim-uk-essen/geberta-xlarge",
          "dbmdz/bert-base-german-uncased",
          "google-bert/bert-base-multilingual-uncased",
          "google-bert/bert-base-multilingual-cased"]

for model in models:
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModel.from_pretrained(model)
