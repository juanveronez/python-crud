from sqlalchemy import func
from sqlalchemy import Column, Integer, String, DateTime

from db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    name = Column(String)
    types = Column(String)
    created_at = Column(DateTime, default=func.now())