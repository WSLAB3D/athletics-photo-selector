def test_basic():
    assert 1 + 1 == 2
    
def test_model_loading():
    from app.detect_objects import load_model
    model = load_model("models/default_model.pt", device="cpu")
    assert model is not None

def test_score_image_mock():
    from app.score_image import score_image
    import numpy as np
    dummy_image = np.zeros((224, 224, 3), dtype=np.uint8)
    score = score_image(dummy_image, model=None)  # mock model
    assert isinstance(score, float)
