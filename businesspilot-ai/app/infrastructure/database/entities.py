from app.infrastructure.database.base import Base 
from app.infrastructure.database.mixins import (
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
)

class BaseEntity(
    UUIDMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    __abstract__ = True