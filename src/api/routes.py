from fastapi import APIRouter

router = APIRouter()

@router.get("/api/models")
async def get_available_models():
    """Get list of available models"""
    return {
        "models": [
            {"id": "anime_kawai", "name": "Anime Kawaii Diffusion", "type": "anime"},
            {"id": "aom3", "name": "AbyssOrangeMix3 (AOM3)", "type": "anime"},
            {"id": "anything_v5", "name": "Anything V5", "type": "anime"},
            {"id": "animagine_xl", "name": "Animagine XL 3.1", "type": "anime"},
            {"id": "photon", "name": "Photon (Realistic)", "type": "realistic"},
        ]
    }

@router.get("/api/styles")
async def get_available_styles():
    """Get list of available style presets"""
    return {
        "styles": [
            {"id": "dynamic", "name": "Dynamic", "description": "Vibrant and energetic"},
            {"id": "cinematic", "name": "Cinematic", "description": "Movie-like composition"},
            {"id": "anime", "name": "Anime", "description": "Japanese animation style"},
            {"id": "photorealistic", "name": "Photorealistic", "description": "Realistic photos"},
        ]
    }

@router.get("/api/upscalers")
async def get_available_upscalers():
    """Get list of available upscaling methods"""
    return {
        "upscalers": [
            {"id": "swinir", "name": "SwinIR", "type": "ai", "quality": "high"},
            {"id": "realesrgan", "name": "Real-ESRGAN", "type": "ai", "quality": "high"},
            {"id": "lanczos", "name": "Lanczos", "type": "traditional", "quality": "medium"},
        ]
    }
