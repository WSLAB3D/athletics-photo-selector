from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

prompts = [
    "runner crossing finish line",
    "athlete celebrating",
    "intense competition",
    "track and field action"
]

def clip_score(img_path):
    image = Image.open(img_path).convert("RGB")
    inputs = processor(text=prompts, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    scores = logits_per_image.softmax(dim=1).detach().numpy()[0]
    return {"clip_score": float(max(scores))}
