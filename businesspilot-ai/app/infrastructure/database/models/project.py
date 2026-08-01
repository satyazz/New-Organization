from __future__ import annotations 
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from app.infrastructure.database.entities import BaseEntity

class Project(BaseEntity):
    __tablename__ = "projects"
    project_name : Mapped[str] = mapped_column (
        String(255),
        nullable=False,
    )
    description : Mapped[str] = mapped_column (
        String (100),
        nullable=True,
    )
    client_id : Mapped[str] = mapped_column (
        ForeignKey("clients.id"),
        nullable=False,
        index=True,
    )
    client: Mapped["Client"] = relationship(
        back_populates="projects",
    )