from fastapi import FastAPI

app = FastAPI(
    title='DDD API',
    description='A restful API for system notification using Domain-Driven Design principles.',
    version='0.0.1',
)


@app.get("/health", tags=["Health"])
async def health():
    return "Healthy"
