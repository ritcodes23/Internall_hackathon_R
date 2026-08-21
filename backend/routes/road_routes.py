from fastapi import APIRouter

router = APIRouter(
    prefix="/roads",
    tags=["Roads"]
)


@router.get("/")
def get_roads():
    return {
        "message": "Road API is working",
        "roads": []
    }


@router.get("/{road_id}")
def get_road(road_id: int):
    return {
        "road_id": road_id,
        "status": "healthy"
    }