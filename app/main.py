import os
import shutil
import torch
from app.detect_objects import detect_objects
from app.score_image import score_image
from app.select_top_images import select_top_images
from app.utils import load_image, get_image_paths

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH", "models/default_model.pt")
DEVICE = os.getenv("DEVICE", "cpu")

# Load model with error handling
try:
    model = torch.load(MODEL_PATH, map_location=DEVICE)
    model.eval()
except Exception as e:
    print(f"❌ Failed to load model from {MODEL_PATH}: {e}")
    exit(1)

# Get image paths
image_dir = "app/images"
image_paths = get_image_paths(image_dir)

# Score and select images
scored_images = []
for image_path in image_paths:
    try:
        image = load_image(image_path)
        score = score_image(image, model)
        scored_images.append((image_path, score))
    except Exception as e:
        print(f"⚠️ Skipping {image_path}: {e}")

# Select top images
selected_images = select_top_images(scored_images, top_k=10)

# Save to output folder
os.makedirs("output", exist_ok=True)
for img_path in selected_images:
    try:
        shutil.copy(img_path, "output/")
        print(f"✅ Saved: {img_path}")
    except Exception as e:
        print(f"❌ Failed to save {img_path}: {e}")
