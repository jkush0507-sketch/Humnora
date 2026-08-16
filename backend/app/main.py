from fastapi import FastAPI

app = FastAPI(
    title="Humnora API",
    description="Emergency response and human assistance platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "Humnora",
        "status": "online",
        "message": "Humnora API is running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "humnora-api",
    }