from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship

from app.db.base import Base


class Business(Base):
    __tablename__ = "businesses"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(255),
        nullable=False,
    )

    description = Column(
        String(1000),
        nullable=True,
    )

    industry = Column(
        String(100),
        nullable=True,
    )

    phone = Column(
        String(20),
        nullable=True,
    )

    email = Column(
        String(255),
        nullable=True,
    )

    website = Column(
        String(255),
        nullable=True,
    )

    address = Column(
        String(500),
        nullable=True,
    )

    logo_url = Column(
        String(500),
        nullable=True,
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    owner = relationship(
        "User",
        back_populates="businesses",
    )

    documents = relationship(
        "Document",
        back_populates="business",
        cascade="all, delete-orphan",
    )