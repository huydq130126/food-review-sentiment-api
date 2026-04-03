import torch
import yaml

#Read config
from transformers import AutoTokenizer, AutoModelForSequenceClassification
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
model_path = config["model_path"]

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
