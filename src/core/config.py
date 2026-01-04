"""
Configuration management for I.R.I.S.
"""
from pathlib import Path
from typing import Optional
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]

env_path = BASE_DIR / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    load_dotenv()

class Config:
    """Central configuration management"""
    
    # Paths
    BASE_DIR = BASE_DIR
    STATIC_DIR = BASE_DIR / "static"
    OUTPUTS_DIR = BASE_DIR / "outputs"
    LOGS_DIR = BASE_DIR / "Logs"
    CONFIG_DIR = STATIC_DIR / "config"
    DATA_DIR = STATIC_DIR / "data"
    
    # Server settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    
    # Discord settings
    DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
    DISCORD_BOT_ID = os.getenv("DISCORD_BOT_ID", "0")
    DISCORD_BOT_OWNER_ID = os.getenv("DISCORD_BOT_OWNER_ID", "0")
    
    DISCORD_CHANNEL_NEW_IMAGES = int(os.getenv("DISCORD_CHANNEL_NEW_IMAGES", "0"))
    DISCORD_CHANNEL_VARIATIONS = int(os.getenv("DISCORD_CHANNEL_VARIATIONS", "0"))
    DISCORD_CHANNEL_UPSCALED = int(os.getenv("DISCORD_CHANNEL_UPSCALED", "0"))
    
    # Model settings
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "anime")
    
    # Upscaler configuration
    DEFAULT_UPSCALER = os.getenv("DEFAULT_UPSCALER", "realesrgan")  # Options: swinir, realesrgan, lanczos
    ENABLE_SWINIR = os.getenv("ENABLE_SWINIR", "true").lower() == "true"
    
    # DRAM Extension
    DRAM_EXTENSION_ENABLED = os.getenv("DRAM_EXTENSION_ENABLED", "false").lower() == "true"
    VRAM_THRESHOLD_GB = float(os.getenv("VRAM_THRESHOLD_GB", "6"))
    MAX_DRAM_GB = int(os.getenv("MAX_DRAM_GB", "16"))
    
    @classmethod
    def read_config_file(cls, filename: str) -> Optional[str]:
        """Read configuration from a file in static/config folder"""
        filepath = cls.CONFIG_DIR / filename
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if not content:
                    return None
                return content
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Warning: Error reading config file {filename}: {e}")
            return None
    
    @classmethod
    def ensure_directories(cls):
        """Ensure all required directories exist"""
        try:
            cls.STATIC_DIR.mkdir(exist_ok=True)
            cls.OUTPUTS_DIR.mkdir(exist_ok=True)
            cls.LOGS_DIR.mkdir(exist_ok=True)
            cls.CONFIG_DIR.mkdir(parents=True, exist_ok=True)
            cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Warning: Error creating directories: {e}")

try:
    Config.ensure_directories()
except Exception as e:
    print(f"Warning: Failed to ensure directories: {e}")
