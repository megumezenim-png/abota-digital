from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from os import getenv
from sqlalchemy import text
from sqlalchemy.orm import Session
from .database import engine
from .models import Group

app = FastAPI(title="ABOTA Digital API", version="0.1.0", docs_url="/api/docs", openapi_url="/api/openapi.json")
origins = [origin.strip() for origin in getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if origin.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["GET", "POST", "PATCH", "DELETE"], allow_headers=["*"])


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="abota-api")


@app.get("/health/db")
def database_health() -> dict:
    if engine is None:
        raise HTTPException(status_code=503, detail="DATABASE_URL não está configurada")
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Não foi possível ligar à base de dados") from exc


@app.get("/api/v1/groups")
def list_groups() -> dict:
    """Lista os grupos persistidos; o modo sem BD devolve 503, nunca dados fictícios."""
    if engine is None:
        raise HTTPException(status_code=503, detail="DATABASE_URL não está configurada")
    try:
        with Session(engine) as session:
            groups = session.query(Group).order_by(Group.id).all()
            return {"items": [{"id": group.id, "name": group.name, "currency": group.currency,
                               "monthly_contribution": str(group.monthly_contribution),
                               "beneficiaries_per_month": group.beneficiaries_per_month}
                              for group in groups]}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Não foi possível consultar os grupos") from exc
