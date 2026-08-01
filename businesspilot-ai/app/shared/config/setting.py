"""
Application Configuration

This module is the single source of truth for all application settings.

"""

from functools import lru_cache

from pydantic import Field 
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
     # project_name :str = ""
     # app_version :str = ""
     # environment:str = ""
     # debug: bool =True
     
     """
    Enterprise application settings.

    Values are loaded from environment variables
    and validated automatically.
    """
     model_config = SettingsConfigDict(
          env_file=".env",
          env_file_encoding="utf-8",
          case_sensitive="False",
          extra="ignore"
     )    
     # =========================
     # Application
     # ==========================
     APP_NAME : str = "ai_models"
     APP_VERSION : str = "0.10"
     DUBEG : bool = True
     ENVEIROMENT : str = "development"
     # =========================
     # Server
     # ==========================
     HOST :str = " "
     PROT : int = 8000
     # =========================
     # AI
     # ==========================
     DEFAULT_MODEL : str = "llama3"
     TEMPERATURE : float = Field(
          default=0.2,
          ge=0,
          le=1,
     )

     DATA_BASE_URL : str = ("postgresql://postgres:password@localhost:5432/ai_business_os")

     # =========================
     # Logging
     # ==========================

     LOG_LEVEL :str = "INFO"

@lru_cache
def get_settings() -> Settings:
     """
    Returns one cached Settings instance.

    This prevents reloading the .env file
    multiple times.
    """
     return Settings()
settings = get_settings()