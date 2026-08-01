"""
"""

from fastapi import FastAPI 
from app.api.router import api_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="BusinessPilot Ai",
        version="0.1.0",
        description="Enterprise AI Platform"
    )
    app.include_router(api_router)
    return app
