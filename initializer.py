import os, requests
from transformers import AutoModel, AutoTokenizer, AutoModelWithLMHead

## download the pre-trained models
models = ["dbmdz/bert-base-german-cased", "T-Systems-onsite/cross-en-de-roberta-sentence-transformer"]

for model in models:
    tokenizer = AutoTokenizer.from_pretrained(model)
    dl_model = AutoModel.from_pretrained(model)