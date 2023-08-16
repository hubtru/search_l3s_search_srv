import os, requests
from transformers import AutoModel, AutoTokenizer, AutoModelWithLMHead

## download the pre-trained models
models = ["dbmdz/bert-base-german-cased", "xlm-roberta-base", "dbmdz/german-gpt2-faust"]

for model in models:
    tokenizer = AutoTokenizer.from_pretrained(model)