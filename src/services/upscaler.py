"""Image upscaling service for I.R.I.S."""
from PIL import Image
import torch
from pathlib import Path
import numpy as np
import cv2

from ..utils.logger import logger


class UpscalerService:
    """Handles image upscaling operations"""
    
    def __init__(self, model_loader):
        self.model_loader = model_loader
        
    def upscale_with_realesrgan(self, image: Image.Image, scale: int = 2) -> Image.Image:
        """Upscale using Real-ESRGAN"""
        if not self.model_loader.upscaler:
            raise RuntimeError("Real-ESRGAN not available")
        
        # Convert PIL to numpy
        img_array = np.array(image)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        # Upscale
        output, _ = self.model_loader.upscaler.enhance(img_array, outscale=scale)
        
        # Convert back to PIL
        output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        return Image.fromarray(output)
    
    def upscale_with_swinir(self, image: Image.Image, scale: int = 2) -> Image.Image:
        """Upscale using SwinIR (higher quality, slower)"""
        if not self.model_loader.swinir_model:
            raise RuntimeError("SwinIR not available")
        
        # Convert PIL to tensor
        img_array = np.array(image).astype(np.float32) / 255.0
        img_tensor = torch.from_numpy(img_array).permute(2, 0, 1).unsqueeze(0)
        img_tensor = img_tensor.to(self.model_loader.device)
        
        # Upscale with SwinIR
        with torch.no_grad():
            output_tensor = self.model_loader.swinir_model(img_tensor)
        
        # Convert back to PIL
        output_array = output_tensor.squeeze(0).permute(1, 2, 0).cpu().numpy()
        output_array = (output_array * 255.0).clip(0, 255).astype(np.uint8)
        
        # Handle different scales
        if scale != 4:  # SwinIR is typically 4x, adjust if needed
            output_img = Image.fromarray(output_array)
            target_size = (image.width * scale, image.height * scale)
            return output_img.resize(target_size, Image.Resampling.LANCZOS)
        
        return Image.fromarray(output_array)
        
    def upscale_with_lanczos(self, image: Image.Image, scale: int = 2) -> Image.Image:
        """Upscale using Lanczos interpolation (fallback)"""
        new_width = image.width * scale
        new_height = image.height * scale
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    def upscale(self, image: Image.Image, scale: int = 2, method: str = "realesrgan") -> Image.Image:
        """Upscale image using specified method
        
        Args:
            image: Input PIL Image
            scale: Upscaling factor (2, 4, or 8)
            method: Upscaling method ('realesrgan', 'swinir', or 'lanczos')
        """
        try:
            if method == "swinir" and self.model_loader.swinir_model:
                logger.info(f"Using SwinIR upscaling at {scale}x...")
                return self.upscale_with_swinir(image, scale)
                
            elif method == "realesrgan" and self.model_loader.upscaler:
                logger.info(f"Using Real-ESRGAN upscaling at {scale}x...")
                return self.upscale_with_realesrgan(image, scale)
                
            else:
                logger.info(f"Using Lanczos upscaling at {scale}x...")
                return self.upscale_with_lanczos(image, scale)
                
        except Exception as e:
            logger.warning(f"{method} upscaling failed: {e}, falling back to Lanczos")
            return self.upscale_with_lanczos(image, scale)
