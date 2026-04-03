yaml_config = """
model_path: "nlptown/bert-base-multilingual-uncased-sentiment"
"""

with open("config.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_config)

print("config.yaml created!")