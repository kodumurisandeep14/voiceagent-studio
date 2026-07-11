from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    BigInteger,
)

from sqlalchemy.orm import relationship

from app.db.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    filename = Column(
        String(255),
        nullable=False,
    )

    original_filename = Column(
        String(255),
        nullable=False,
    )

    file_type = Column(
        String(50),
        nullable=False,
    )

    file_size = Column(
        BigInteger,
        nullable=False,
    )

    file_path = Column(
        String(500),
        nullable=False,
    )

    upload_date = Column(
        DateTime,
        default=datetime.utcnow,
    )

    business_id = Column(
        Integer,
        ForeignKey("businesses.id"),
        nullable=False,
    )

    business = relationship(
        "Business",
        back_populates="documents",
    )