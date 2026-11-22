from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from os import getenv

app = FastAPI(title="ABOTA Digital API", version="0.1.0", docs_url="/api/docs", openapi_url="/api/openapi.json")
origins = [origin.strip() for origin in getenv("CORS_ORIGINS", "http://localhost:3000").split(",") if origin.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["GET", "POST", "PATCH", "DELETE"], allow_headers=["*"])


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="abota-api")


@app.get("/api/v1/groups")
def list_groups() -> dict:
    """Endpoint de arranque. Os dados reais dependem da ligação PostgreSQL/migrações."""
    return {"items": [], "mode": "empty-unconfigured"}
