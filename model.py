import torch
import yaml
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification

#Read config
class SentimentClassification:
    def __init__(self, config_path):
        config_file = Path(config_path)
        if not config_file.is_absolute():
            config_file = (Path(__file__).resolve().parent / config_file).resolve()

        with open(config_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        model_path = config["model_path"]

        #load tokenizer + model
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)

    def __call__(self, message):
        #text to tensor
        inputs = self.tokenizer(message, return_tensors="pt")

        #run model
        with torch.no_grad():
            logits = self.model(**inputs).logits
        
        predicted_class_id = logits.argmax().item()
        label = self.model.config.id2label[predicted_class_id]
        probs = torch.softmax(logits, dim=-1)
        confidence = probs.max().item()

        label_map = {
            "1 star" : "Rất dở",
            "2 stars" : "Dở",
            "3 stars" : "Bình Thường",
            "4 stars" : "Ngon",
            "5 stars" : "Rất ngon"
        }

        return {
            "rating": label,
            "meaning": label_map.get(label, label),
            "confidence": round(confidence, 4)
        }
