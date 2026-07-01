from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    role = Column(String(20), nullable=False)

    content = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id"),
        nullable=False
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )