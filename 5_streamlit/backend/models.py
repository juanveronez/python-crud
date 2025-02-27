from sqlalchemy import Column, Integer, String, Float, DateTime, func

from database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Float)
    category = Column(String)
    email_supplier = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())