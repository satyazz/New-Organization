from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from app.shared.config.setting import settings

engine = create_engine (
    settings.DATA_BASE_URL,
    pool_pre_ping=True,  
)
sessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False, 
)