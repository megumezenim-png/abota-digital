from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def _database_url() -> str | None:
    url = getenv("DATABASE_URL")
    if not url:
        return None
    if url.startswith("postgres://"):
        url = "postgresql://" + url.removeprefix("postgres://")
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


url = _database_url()
engine = create_engine(url, pool_pre_ping=True) if url else None
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False) if engine else None


def get_db():
    if SessionLocal is None:
        raise RuntimeError("DATABASE_URL não está configurada")
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
