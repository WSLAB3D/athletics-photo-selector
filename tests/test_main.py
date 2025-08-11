import os
import pytest
import numpy as np
from app.score_image import score_image
from app.select_top_images import select_top_images
from app.utils import get_image_paths, load_image

def test_get_image_paths_returns_list():
    paths = get_image_paths("app/images")
    assert isinstance(paths, list)

def test_load_image_returns_array():
    paths = get_image_paths("app/images")
    if paths:
        img = load_image(paths[0])
        assert isinstance(img, np.ndarray)

def test_score_image_with_dummy_input():
    dummy_image = np.zeros((224, 224, 3), dtype=np.uint8)
    score = score_image(dummy_image, model=None)  # Assuming fallback scoring
    assert isinstance(score, float)

def test_select_top_images():
    dummy_scores = [("img1.jpg", 0.9), ("img2.jpg", 0.5), ("img3.jpg", 0.8)]
    top_images = select_top_images(dummy_scores, top_k=2)
    assert top_images == ["img1.jpg", "img3.jpg"]

def test_model_path_exists():
    model_path = os.getenv("MODEL_PATH", "models/default_model.pt")
    assert os.path.exists(model_path), f"Model path not found: {model_path}"
    
def test_load_image_with_resize_and_normalization():
    paths = get_image_paths("app/images")
    if paths:
        img = load_image(paths[0], target_size=(224, 224), normalize=True)
        assert img.shape == (224, 224, 3)
        assert img.max() <= 1.0 and img.min() >= 0.0