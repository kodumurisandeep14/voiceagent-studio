from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, HttpUrl


class BusinessCreate(BaseModel):
    name: str
    description: Optional[str] = None
    industry: str
    phone: str
    email: EmailStr
    website: Optional[HttpUrl] = None
    address: str
    logo_url: Optional[HttpUrl] = None


class BusinessUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    website: Optional[HttpUrl] = None
    address: Optional[str] = None
    logo_url: Optional[HttpUrl] = None


class BusinessResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    industry: str
    phone: str
    email: EmailStr
    website: Optional[HttpUrl]
    address: str
    logo_url: Optional[HttpUrl]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)