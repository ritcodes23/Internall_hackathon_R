from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.road_routes import router as road_router

app = FastAPI(
    title="Infra-Predict API",
    description="Predictive infrastructure maintenance system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(road_router)

@app.get("/")
def home():
    return {
        "message": "Infra-Predict API is running",
        "supported_infrastructure": ["roads", "bridges"]
    }