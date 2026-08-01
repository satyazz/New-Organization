import uuid
from sqlalchemy import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import Boolean
from __future__ import annotations

class UUIDMixin:
    """
    Provides UUID primary key.
    """
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

class TimestampMixin : 
    create_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),server_default=func.now(),
        nullable=False,
    )
    update_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
class SoftDeleteMixin:
    is_deleted : Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    ) 
    deleted_at : Mapped [datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )
    def mark_as_deleted(self) -> None:
        """
        Mark the entity as soft deleted.
        """
        self.is_deleted = True
        self.deleted_at = datetime.utcnow()

    def restore(self) -> None:
        """
        Restore a previously soft-deleted entity.
        """
        self.is_deleted = False
        self.deleted_at = None

