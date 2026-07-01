from fastapi import FastAPI

app = FastAPI(
    title="VoiceAgent Studio API",
    description="Backend API for VoiceAgent Studio",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {
        "application": "VoiceAgent Studio",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }