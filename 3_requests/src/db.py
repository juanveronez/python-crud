from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase

SQLALCHEMY_DATABASE_URL = 'sqlite:///pokemon.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base: DeclarativeBase = declarative_base()
