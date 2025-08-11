import os
import torch
from dotenv import load_dotenv
from app.utils import get_image_paths, load_image

# Load environment variables
load_dotenv()
MODEL_PATH = os.getenv("MODEL_PATH", "models/default_model.pt")
DEVICE = os.getenv("DEVICE", "cpu")

# Detect GPU
if torch.cuda.is_available():
    print(f"✅ GPU detected: {torch.cuda.get_device_name(0)}")
else:
    print("🚫 No GPU detected. Running on CPU.")

# Load model
# print(f"📦 Loading model from: {MODEL_PATH}")
# model = torch.load(MODEL_PATH, map_location=DEVICE)
# model.eval()
from torchvision.models import resnet50, ResNet50_Weights

# Load pretrained ResNet50 model and preprocessing transforms
print(f"📦 Loading ResNet50 model")
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()

preprocess = weights.transforms()



# Load and preprocess images
image_folder = "app/images"
image_paths = get_image_paths(image_folder)
print(f"🖼️ Found {len(image_paths)} images in {image_folder}")

# for path in image_paths:
#     try:
#         img = load_image(path, target_size=(224, 224), normalize=True)
#         tensor = torch.tensor(img).permute(2, 0, 1).unsqueeze(0).to(DEVICE)  # Shape: [1, 3, H, W]
#         with torch.no_grad():
#             output = model(tensor)
#         print(f"✅ Inference for {os.path.basename(path)}: {output}")
#     except Exception as e:
#         print(f"❌ Error processing {path}: {e}")

for path in image_paths:
    try:
        input_tensor = load_and_preprocess(path).to(DEVICE)
        with torch.no_grad():
            output = model(input_tensor)
        predicted_class = output.argmax(dim=1).item()
        print(f"{os.path.basename(path)} → class {predicted_class}")
    except Exception as e:
        print(f"Error processing {path}: {e}")
