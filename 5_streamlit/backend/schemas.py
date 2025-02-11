from pydantic import BaseModel, PositiveFloat, PositiveInt, EmailStr, PastDatetime
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str = None
    price: PositiveFloat
    category: str
    email_supplier: EmailStr

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: PositiveInt
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(ProductBase):
    name: str = None
    description: str = None
    price: PositiveFloat = None
    category: str = None
    email_supplier: EmailStr = None