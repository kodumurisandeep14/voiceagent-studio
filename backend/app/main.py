from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine
from app.api.users import router as user_router

app = FastAPI(
    title="VoiceAgent Studio API",
    version="1.0.0"
)

app.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
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