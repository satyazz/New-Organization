"""
"""

from fastapi import FastAPI 
from app.api.router import api_router
from app.shared.config.setting import settings

def create_app() -> FastAPI:
    # settings = get_settings()
    app = FastAPI(
        title= settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DUBEG
    )
    app.include_router(api_router)
    return app
