import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_path = "nlptown/bert-base-multilingual-uncased-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

text = "Quán này rất ngon"
inputs = tokenizer(text, return_tensors = "pt")
