# 🧠 AI App with CPU/GPU Docker Profiles

This project is a containerized Python application designed to run seamlessly on both CPU and GPU environments. It uses Docker and `docker-compose` profiles to toggle between hardware configurations.

---

## 🚀 Features

- ✅ Profile-based Docker builds for CPU and GPU
- 🐍 Python environment with customizable dependencies
- 🐳 Clean Dockerfile with build-time flexibility
- ⚙️ GPU support via NVIDIA runtime
- 📦 Optional `.env` file for runtime configuration

---

## 📁 Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
├── .env
└── README.md
```

---

## 🐳 Docker Setup

### 🔧 Build and Run with CPU

```bash
docker compose --profile cpu up --build
```

This uses a lightweight Python base image (`python:3.10-slim`) and runs the app in a CPU-only environment.

---

### ⚡ Build and Run with GPU

```bash
docker compose --profile gpu up --build
```

This uses a PyTorch GPU-enabled image (`pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime`) and enables the NVIDIA runtime for GPU acceleration.

> 🧠 Make sure you have the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed to use GPU containers.

---

## ⚙️ Environment Configuration

You can customize runtime behavior using a `.env` file:

```env
MODEL_PATH=models/default_model.pt
DEVICE=auto
```

In your Python code:

```python
import os

device = os.getenv("DEVICE", "cpu")
model_path = os.getenv("MODEL_PATH", "models/default_model.pt")

print(f"Running on device: {device}")
print(f"Using model: {model_path}")
```

---

## 📦 Installing Dependencies

Dependencies are managed via `requirements.txt`. To update:

```bash
pip freeze > requirements.txt
```

---

## 🧪 GPU Detection (Optional)

You can add this to `main.py` to auto-detect GPU availability:

```python
import torch

if torch.cuda.is_available():
    print(f"✅ GPU detected: {torch.cuda.get_device_name(0)}")
else:
    print("🚫 No GPU detected. Running on CPU.")
```

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🙌 Contributing

Feel free to fork, submit issues, or open pull requests. Contributions are welcome!
