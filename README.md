# 🏃 Athletics Photo Selector

An AI-powered pipeline to analyze and select top-quality photos from athletic events. Designed for speed, scalability, and simplicity—with support for CPU and GPU environments via Docker.

---

## 📦 Features

- 🔍 Automatic image loading and preprocessing
- 🧠 PyTorch model inference on athletic photos
- 🐳 Docker support for CPU and GPU environments
- ⚙️ Environment configuration via `.env`
- 🧪 Unit tests for core utilities

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/WSLAB3D/athletics-photo-selector.git
cd athletics-photo-selector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your images

Place your `.jpg`, `.png`, etc. files in:

```
app/images/
```

### 4. Configure environment

Create a `.env` file in the root directory:

```env
MODEL_PATH=models/default_model.pt
DEVICE=auto
```

---

## 🚀 Run the pipeline

```bash
python main.py
```

This will:

- Load all images from `app/images`
- Resize to 224×224 and normalize pixel values
- Run inference using your PyTorch model
- Print predictions for each image

---

## 🧪 Run tests

```bash
pytest tests/
```

---

## 🐳 Docker Usage

### CPU

```bash
docker compose --profile cpu up --build
```

### GPU

```bash
docker compose --profile gpu up --build
```

> ⚠️ Requires NVIDIA Container Toolkit for GPU support

---

## 📁 Project Structure

```
athletics-photo-selector/
├── app/
│   ├── images/          # Input images
│   └── utils.py         # Image loading and preprocessing
├── main.py              # Pipeline entry point
├── tests/               # Unit tests
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container setup
├── docker-compose.yml   # Profiles for CPU/GPU
├── .env                 # Runtime config
└── README.md            # Project overview
```

---

## 📜 License

MIT — feel free to use, modify, and contribute!

---

## 🤝 Contributing

Pull requests welcome! For major changes, open an issue first to discuss what you’d like to improve.
