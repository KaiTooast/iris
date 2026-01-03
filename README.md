# 🌌 I.R.I.S. Engine
### Intelligent Rendering & Image Synthesis

**A modular, local-first AI image generation engine — built to be forked, extended, and owned.**

I.R.I.S. Engine is an **open-source AI image generation platform** designed as a **foundation**, not a locked product.  
Think of it as **Linux for AI image generation**:

> You get a fully working system —  
> but *you* decide how it evolves.

⚠️ **Runs entirely on your own hardware**  
No cloud. No accounts. No telemetry. No vendor lock-in.

---

![Python](https://img.shields.io/badge/python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-green)
![WebSockets](https://img.shields.io/badge/WebSockets-realtime-purple)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/status-active%20development-orange)

---

## ✨ Core Philosophy

- 🧠 **Local-first** — everything runs on your machine
- 🔓 **Open Source** — modify, fork, redistribute
- 🧩 **Modular architecture** — UI, backend, models are replaceable
- 🧪 **Experiment-friendly** — designed for tinkering & research
- 🚀 **Production-capable** — APIs, WebSockets, scaling-ready

This repository provides a **fully functional reference implementation**, not a closed product.

---

## 🖼️ Feature Overview

### Core Features
- Modern **Web UI** (Generate, Gallery, Settings)
- **Multiple AI models** (anime, realistic, pixel art, SDXL)
- **Text-to-Image** & **Image-to-Image**
- **Real-time progress streaming** (WebSockets)
- **Prompt & image history logging**
- **NSFW prompt filtering**
- **CPU & low-VRAM GPU support**

### Advanced Features
- **DRAM Extension** (system RAM fallback for low VRAM GPUs)
- **Custom resolutions** (256×256 → 4096×4096)
- **CFG scale & sampling control**
- **Real-ESRGAN upscaling** (2× / 4× / 8×)
- **Live gallery updates**
- **Automatic VRAM safety adjustments**
- **Optional Discord bot integration**

---

## 🚀 Quick Start

### Requirements
```

Python 3.9 – 3.11
GPU recommended (4 GB VRAM minimum)
CUDA 11.8+ optional (CPU mode supported)

````

### Installation
```bash
git clone https://github.com/KaiTooast/iris-engine.git
cd iris-engine

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
````

### Run

```bash
# Web UI only
python src/start.py web

# Discord bot only
python src/start.py bot

# Everything
python src/start.py all
```

🌐 Open: **[http://localhost:8000](http://localhost:8000)**

---

## 🧩 Project Structure

```
src/
├── api/            # FastAPI + WebSocket backend
├── core/           # Model loading & generation logic
├── services/       # Discord, upscaling, extensions
├── utils/          # Logging, file handling
├── frontend/       # HTML UI (Generate, Gallery, Settings)
└── start.py        # Unified entry point
```

Static data, outputs, and logs are **explicitly separated** to encourage modification.

---

## ⚙️ Configuration

Example `.env` file:

```env
HOST=0.0.0.0
PORT=8000

DEFAULT_MODEL=anime_kawai

DRAM_EXTENSION_ENABLED=false
VRAM_THRESHOLD_GB=6
MAX_DRAM_GB=16
```

All services (including Discord) are **optional and isolated**.

---

## 🧠 Designed for Modification

You are explicitly encouraged to:

* Replace the frontend entirely
* Add your own models or pipelines
* Build a token or subscription system
* Deploy in a private or public datacenter
* Run on NVIDIA, AMD, or Intel GPUs (experimental)
* Fork this into a commercial or closed product

**I.R.I.S. Engine does not enforce a business model.**

---

## 🖥️ Hardware Reference

| Tier        | GPU      | VRAM  | Notes              |
| ----------- | -------- | ----- | ------------------ |
| Minimum     | GTX 1650 | 4 GB  | Tested & supported |
| Recommended | RTX 3060 | 12 GB | Smooth experience  |
| High-End    | RTX 4090 | 24 GB | Near real-time     |

> The engine was **tested on a GTX 1650**, proving functionality on low-end hardware.

---

## 🔌 API & WebSocket Support

* REST API for generation, gallery, system info
* WebSocket streams for:

  * Generation progress
  * Gallery updates
  * Multi-page synchronization

Perfect for **custom frontends**, automation, or external clients.

---

## 🛡️ Safety

* Prompt-based NSFW filtering
* Explicit content blocking
* Category-based detection
* Easily extendable or disableable

---

## 📜 License

**Creative Commons Attribution 4.0 (CC BY 4.0)**

You may use, modify, redistribute, and commercialize this project —
**attribution is required.**

See `LICENSE` for details.

---

## 🤝 Contributing

Contributions are welcome — from small fixes to major architectural changes.

Please read **CONTRIBUTING.md** before submitting a pull request.

---

## 🌍 Final Note

I.R.I.S. Engine is not built to compete with cloud AI platforms.

It exists to **give control back** to developers and creators.

If you value:

* ownership over subscriptions
* experimentation over lock-in
* transparency over black boxes

then this project is for you.
