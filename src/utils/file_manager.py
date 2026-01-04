"""
File management utilities for I.R.I.S.
"""
from pathlib import Path
from datetime import datetime
import json
from typing import Optional, Dict, List
from PIL import Image

try:
    from src.core.config import Config
except ImportError:
    Config = None

class FileManager:
    """Manage file operations and naming"""
    
    @staticmethod
    def generate_filename(
        prefix: str = "img",
        seed: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        extension: str = "png"
    ) -> str:
        """
        Generate a standardized filename
        Format: {prefix}_{timestamp}_{seed}_{width}x{height}.{extension}
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        parts = [prefix, timestamp]
        
        if seed is not None:
            parts.append(str(seed))
        
        if width and height:
            parts.append(f"{width}x{height}")
        
        filename = "_".join(parts) + f".{extension}"
        return filename
    
    @staticmethod
    def save_json(filepath: Path, data: Dict or List):
        """Save data to JSON file with error handling"""
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise IOError(f"Failed to save JSON to {filepath}: {e}")
    
    @staticmethod
    def load_json(filepath: Path) -> Dict or List:
        """Load data from JSON file with error handling"""
        if not filepath.exists():
            return {}
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {filepath}: {e}")
        except Exception as e:
            raise IOError(f"Failed to load JSON from {filepath}: {e}")
    
    @staticmethod
    def log_prompt(prompt: str, settings: Dict):
        """Log prompt to prompts_history.json"""
        if Config is None:
            return
            
        log_file = Config.DATA_DIR / "prompts_history.json"
        
        try:
            # Load existing prompts
            prompts = []
            if log_file.exists():
                prompts = FileManager.load_json(log_file)
                if not isinstance(prompts, list):
                    prompts = []
            
            # Add new prompt
            prompts.append({
                "timestamp": datetime.now().isoformat(),
                "prompt": prompt,
                "settings": settings
            })
            
            if len(prompts) > 1000:
                prompts = prompts[-1000:]
            
            # Save
            FileManager.save_json(log_file, prompts)
        except Exception as e:
            print(f"Warning: Failed to log prompt: {e}")
    
    @staticmethod
    def log_sent_image(filename: str, message_link: str):
        """Log sent image to img_send.json"""
        if Config is None:
            return
            
        log_file = Config.DATA_DIR / "img_send.json"
        
        try:
            # Load existing
            sent_images = FileManager.load_json(log_file)
            if not isinstance(sent_images, dict):
                sent_images = {}
            
            # Add new entry
            sent_images[filename] = {
                "message_link": message_link,
                "sent_at": datetime.now().isoformat()
            }
            
            # Save
            FileManager.save_json(log_file, sent_images)
        except Exception as e:
            print(f"Warning: Failed to log sent image: {e}")
    
    @staticmethod
    def get_sent_images() -> Dict:
        """Get all sent images"""
        if Config is None:
            return {}
            
        log_file = Config.DATA_DIR / "img_send.json"
        try:
            sent_images = FileManager.load_json(log_file)
            return sent_images if isinstance(sent_images, dict) else {}
        except Exception:
            return {}
    
    @staticmethod
    def save_image(image: Image.Image, filepath: Path) -> Path:
        """Save PIL Image to file"""
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            image.save(filepath, format="PNG", optimize=True)
            return filepath
        except Exception as e:
            raise IOError(f"Failed to save image to {filepath}: {e}")
    
    @staticmethod
    def load_image(filepath: Path) -> Image.Image:
        """Load PIL Image from file"""
        try:
            return Image.open(filepath).convert("RGB")
        except Exception as e:
            raise IOError(f"Failed to load image from {filepath}: {e}")
