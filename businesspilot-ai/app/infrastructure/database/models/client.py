from __future__ import annotations
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column 
from sqlalchemy import String 
from sqlalchemy.orm import  relationship
from app.infrastructure.database.entities import BaseEntity

class Client(BaseEntity):
    __tablename__ = "clients"
    company_name : Mapped[str] = mapped_column (
        String(255),
        nullable=False,
    )
    email : Mapped[str] = mapped_column (
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )
    contact_person : Mapped[str] = mapped_column (
        String(255),
        nullable=False,

    )
    phone : Mapped[str | None] = mapped_column (
        String(20),
        nullable=True,
    )

    country : Mapped[str] = mapped_column (
        String (100),
        nullable= False
    )
    industry : Mapped [str] = mapped_column (
        String(100),
        nullable=True
    )
    projects : Mapped [list["Project"]] = relationship (
        back_populates="client",
        cascade= "all, delete-orphan",
        lazy="selectin"
    )