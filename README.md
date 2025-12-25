# I.R.I.S. (Intelligent Rendering & Image Synthesis)

**High-performance AI image generation powered by Stable Diffusion with Discord integration and web interface.**

![IRIS Banner](examples/Example%20(6).png)

---

## Overview

I.R.I.S. is a powerful, GPU-accelerated AI image generation system that combines Stable Diffusion with an intuitive web interface and Discord bot integration. Generate stunning images from text prompts, create variations, and upscale images—all with seamless Discord sharing capabilities.

### Key Features

- **High-Quality Image Generation** - Stable Diffusion-powered text-to-image synthesis
- **Web Interface** - Modern, user-friendly web UI for easy image generation
- **Discord Integration** - Automatic posting to configurable Discord channels
- **Image Variations** - Create multiple variations from existing images
- **Upscaling** - Enhance image resolution with AI upscaling
- **Prompt History** - Track and reuse successful prompts
- **Flexible Configuration** - Customizable settings for every use case
- **GPU Optimized** - Efficient VRAM management for various GPU capabilities

---

## Documentation

**Comprehensive documentation is available at:** [https://kaitooast.github.io/iris-image-synthesis/](https://kaitooast.github.io/iris-image-synthesis/)

### Quick Links

- [Getting Started](https://kaitooast.github.io/iris-image-synthesis/setup.html) - Installation and setup guide
- [Usage Guide](https://kaitooast.github.io/iris-image-synthesis/usage.html) - How to use I.R.I.S.
- [Prompt Engineering](https://kaitooast.github.io/iris-image-synthesis/prompts.html) - Tips for better prompts
- [FAQ](https://kaitooast.github.io/iris-image-synthesis/faq.html) - Common questions answered
- [Troubleshooting](https://kaitooast.github.io/iris-image-synthesis/troubleshooting.html) - Solve common issues
- [API Reference](https://kaitooast.github.io/iris-image-synthesis/api.html) - API documentation
- [Search Documentation](https://kaitooast.github.io/iris-image-synthesis/search.html) - Search all docs

The documentation includes a powerful search feature that lets you quickly find answers to any questions. Press `/` to activate search from any docs page.

---

## Quick Start

### Prerequisites

- **Python** 3.9 or higher
- **GPU** with CUDA support (NVIDIA recommended)
- **VRAM** 6GB minimum, 8GB+ recommended
- **CUDA** 11.8 or higher
- **Discord Bot Token** (optional, for Discord features)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kaitooast/iris-image-synthesis.git
   cd iris-image-synthesis
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   # Discord Bot Configuration (Optional)
   DISCORD_BOT_TOKEN=your_bot_token_here
   DISCORD_BOT_OWNER_ID=your_discord_user_id
   DISCORD_BOT_ID=bot_user_id
   
   # Discord Channel IDs (Optional)
   DISCORD_CHANNEL_NEW_IMAGES=channel_id
   DISCORD_CHANNEL_VARIATIONS=channel_id
   DISCORD_CHANNEL_UPSCALED=channel_id
   
   # Server Configuration
   SERVER_PORT=8000
   SERVER_HOST=0.0.0.0
   ```

5. **Start I.R.I.S.:**
   ```bash
   # Start web interface only
   python src/start.py web
   
   # Start Discord bot only
   python src/start.py bot
   
   # Start both
   python src/start.py all
   ```

6. **Access the web interface:**
   Open your browser to `http://localhost:8000`

For detailed setup instructions, visit the [Setup Guide](https://kaitooast.github.io/iris-image-synthesis/setup.html).

---

## Usage Examples

### Generate an Image

```python
# Via Web Interface
1. Enter your prompt: "A serene mountain landscape at sunset, photorealistic"
2. Adjust settings (resolution, steps, guidance scale)
3. Click "Generate"
4. Image appears in gallery and optionally posts to Discord
```

### Create Variations

```python
# From existing image
1. Select an image from the gallery
2. Click "Create Variation"
3. Adjust variation strength
4. Generate new variations based on the original
```

### Upscale Images

```python
# Enhance resolution
1. Select an image to upscale
2. Choose upscale factor (2x, 4x)
3. Click "Upscale"
4. High-resolution image is generated
```

More examples and detailed usage instructions are available in the [Usage Guide](https://kaitooast.github.io/iris-image-synthesis/usage.html).

---

## Project Structure

```
IRIS/
├── src/
│   ├── api/                    # FastAPI backend
│   ├── services/               # Discord bot service
│   ├── core/                   # Core generation logic
│   ├── utils/                  # Utilities and helpers
│   └── start.py                # Entry point
├── static/
│   ├── data/                   # JSON data storage
│   ├── config/                 # Configuration files
│   └── assets/                 # Web assets
├── outputs/                    # Generated images
├── docs/                       # Documentation website
├── examples/                   # Example outputs
├── Logs/                       # Application logs
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── README.md                   # This file
```

---

## Configuration

I.R.I.S. offers extensive configuration options for generation parameters, Discord channels, model settings, and performance optimization. See the [Setup Guide](https://kaitooast.github.io/iris-image-synthesis/setup.html) for complete configuration details.

### Key Settings

- **Resolution** - Output image dimensions
- **Steps** - Generation quality (more steps = better quality)
- **Guidance Scale** - How closely to follow the prompt
- **Sampler** - Algorithm for image generation
- **Seed** - For reproducible results
- **Discord Channels** - Separate channels for different image types

---

## GPU Compatibility

I.R.I.S. is optimized for various GPU configurations:

| GPU | VRAM | Recommended Resolution | Notes |
|-----|------|----------------------|-------|
| RTX 4090 | 24GB | Up to 1024x1024 | Optimal performance |
| RTX 3080/4080 | 10-16GB | Up to 768x768 | Excellent performance |
| RTX 3060/3070 | 8-12GB | Up to 512x512 | Good performance |
| RTX 2060/3050 | 6-8GB | Up to 512x512 | May need optimization |

See the [FAQ](https://kaitooast.github.io/iris-image-synthesis/faq.html) for GPU-specific optimization tips.

---

## Discord Integration

I.R.I.S. features powerful Discord integration that automatically shares generated images to configurable channels:

- **New Images** - Fresh generations posted to dedicated channel
- **Variations** - Image variations tracked separately
- **Upscaled** - Enhanced images shared to upscale channel
- **Interactive Commands** - Discord bot commands for generation

Setup instructions are available in the [Setup Guide](https://kaitooast.github.io/iris-image-synthesis/setup.html#discord-setup).

---

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Troubleshooting

Having issues? Check the [Troubleshooting Guide](https://kaitooast.github.io/iris-image-synthesis/troubleshooting.html) for solutions to common problems:

- CUDA/GPU errors
- Memory issues
- Discord connection problems
- Model loading failures
- Image generation errors

You can also search the [documentation](https://kaitooast.github.io/iris-image-synthesis/search.html) for specific error messages.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Stable Diffusion** - Core image generation model
- **Hugging Face** - Model hosting and diffusers library
- **Discord.py** - Discord bot framework
- **FastAPI** - Web backend framework
- **PyTorch** - Deep learning framework

---

## Support

Need help? Here are your options:

- **Documentation** - [https://kaitooast.github.io/iris-image-synthesis/](https://kaitooast.github.io/iris-image-synthesis/)
- **Search Docs** - [Search all documentation](https://kaitooast.github.io/iris-image-synthesis/search.html)
- **Issues** - [GitHub Issues](https://github.com/kaitooast/iris-image-synthesis/issues)
- **Discussions** - [GitHub Discussions](https://github.com/kaitooast/iris-image-synthesis/discussions)

---

## Gallery

![Example 1](examples/Example%20(1).png)
![Example 2](examples/Example%20(2).png)
![Example 3](examples/Example%20(3).png)

More examples available in the [examples](examples/) directory and the [documentation](https://kaitooast.github.io/iris-image-synthesis/).

---

**Made with ❤️ by the I.R.I.S. community**

[Documentation](https://kaitooast.github.io/iris-image-synthesis/) | [Issues](https://github.com/kaitooast/iris-image-synthesis/issues) | [Contributing](CONTRIBUTING.md)
