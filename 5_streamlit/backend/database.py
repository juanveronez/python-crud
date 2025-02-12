from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase

from dotenv import load_dotenv
from os import getenv

load_dotenv()

POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_HOST = getenv("POSTGRES_HOST")
POSTGRES_PORT = getenv("POSTGRES_PORT")

have_host_port = POSTGRES_HOST is not None and POSTGRES_PORT is not None
host = f"{POSTGRES_HOST}:{POSTGRES_PORT}" if have_host_port else "postgres"

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{host}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base: DeclarativeBase = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
