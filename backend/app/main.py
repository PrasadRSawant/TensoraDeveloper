from fastapi import FastAPI

app = FastAPI(
    title="AI/ML Portfolio Backend",
    description="API for AI/ML Engineer Portfolio project",
    version="1.0.0",
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the AI/ML Portfolio Backend!"}