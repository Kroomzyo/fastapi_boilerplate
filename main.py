from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {
        "data": "health_check"
    }

def create_app():
    app = FastAPI(
        debug=True,
        description="Boiler_plate"
    )
    app.include_router(router)

    return app


