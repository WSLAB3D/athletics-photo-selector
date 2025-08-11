import os
import cv2
import numpy as np
from PIL import Image

def load_and_preprocess(path):
    image = Image.open(path).convert("RGB")
    return preprocess(image).unsqueeze(0)  # Shape: [1, 3, 224, 224]

def get_image_paths(folder, extensions=(".jpg", ".jpeg", ".png")):
    """
    Returns a list of image file paths from the specified folder.
    """
    image_paths = []
    for fname in os.listdir(folder):
        if fname.lower().endswith(extensions):
            image_paths.append(os.path.join(folder, fname))
    return image_paths

def load_image(image_path, target_size=None, normalize=True):
    """
    Loads an image from disk, converts to RGB, resizes, and normalizes.

    Args:
        image_path (str): Path to the image file.
        target_size (tuple): Desired size as (width, height). If None, no resizing.
        normalize (bool): Whether to normalize pixel values to [0, 1].

    Returns:
        np.ndarray: Processed image as a NumPy array.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if target_size:
        image = cv2.resize(image, target_size)

    if normalize:
        image = image.astype(np.float32) / 255.0

    return image

