from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, HttpUrl


# ---------------------------------
# Base Schema
# ---------------------------------
class DocumentBase(BaseModel):
    filename: str
    original_filename: str
    file_type: str
    file_size: int
    file_path: str


# ---------------------------------
# Create Document
# ---------------------------------
class DocumentCreate(DocumentBase):
    business_id: int


# ---------------------------------
# Update Document
# ---------------------------------
class DocumentUpdate(BaseModel):
    filename: Optional[str] = None
    original_filename: Optional[str] = None
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    file_path: Optional[str] = None


# ---------------------------------
# Document Response
# ---------------------------------
class DocumentResponse(DocumentBase):
    id: int
    upload_date: datetime
    business_id: int

    model_config = ConfigDict(from_attributes=True)