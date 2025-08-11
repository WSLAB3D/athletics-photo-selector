# 🏃 Athletics Photo Selector

An AI-powered pipeline for selecting high-quality sports photos using object detection and image scoring. Designed to streamline the workflow for photographers and media teams covering athletic events.

## 🚀 Features
- Detects key objects (e.g. athletes) in images
- Scores images based on composition and clarity
- Selects top images from a folder
- Supports CPU and GPU via Docker profiles
- Easily configurable via `.env` file

## 📁 Project Structure
```
.
├── app/
│   ├── detect_objects.py
│   ├── score_image.py
│   ├── select_top_images.py
│   └── images/                # Input images folder
├── tests/
│   └── test-main.py           # Unit tests
├── main.py                    # Pipeline entry point
├── .env                       # Environment variables
├── .flake8                    # Linting config
├── pytest.ini                 # Pytest config
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/WSLAB3D/athletics-photo-selector.git
cd athletics-photo-selector
```

### 2. Add your model
Place your PyTorch model file in the `models/` folder and update the path in `.env`:

```
MODEL_PATH=models/default_model.pt
DEVICE=cuda  # or 'cpu'
```

### 3. Add images
Drop your input images into `app/images/`.

## 🐳 Run with Docker

### CPU
```bash
docker compose --profile cpu up
```

### GPU
```bash
docker compose --profile gpu up
```

## 🧪 Run Tests
```bash
pytest
```
Includes basic unit tests for pipeline components. Extend `tests/test-main.py` to cover edge cases and scoring logic.

## 🧼 Linting
```bash
flake8
```
Configured via `.flake8` to ignore common formatting warnings and exclude irrelevant folders.

## 📜 License
MIT — feel free to use, modify, and contribute.
