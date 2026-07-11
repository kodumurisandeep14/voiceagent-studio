from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine

from app.api.users import router as user_router
from app.api.businesses import router as business_router
from app.api.documents import router as document_router

app = FastAPI(
    title="VoiceAgent Studio API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "VoiceAgent Studio API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/db-test")
def db_test():
    try:
        with engine.connect() as conn:
            version = conn.execute(text("SELECT version()")).scalar()

        return {
            "status": "success",
            "postgres": version,
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e),
        }


# -------------------------
# User APIs
# -------------------------
app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)


# -------------------------
# Business APIs
# -------------------------
app.include_router(
    business_router,
    prefix="/businesses",
    tags=["Businesses"]
)
# -------------------------
# Document APIs
# -------------------------
app.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"]
)