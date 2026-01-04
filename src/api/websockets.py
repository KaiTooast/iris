from fastapi import WebSocket, WebSocketDisconnect
from typing import List
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        """Broadcast message to all connected clients"""
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass

manager = ConnectionManager()

async def broadcast_status(status: str, data: dict = None):
    """Broadcast system status to all connected clients"""
    message = {
        "type": "status",
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "data": data or {}
    }
    await manager.broadcast(message)

async def broadcast_progress(step: int, total_steps: int, current_image: int, total_images: int):
    """Broadcast generation progress to all connected clients"""
    message = {
        "type": "progress",
        "step": step,
        "total_steps": total_steps,
        "current_image": current_image,
        "total_images": total_images,
        "percentage": int((step / total_steps) * 100)
    }
    await manager.broadcast(message)
