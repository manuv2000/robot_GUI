from fastapi import APIRouter
from interfaces.subscriber_interface import RosSubscriberInterface

router = APIRouter()

def register_odom_routes(app, subscriber: RosSubscriberInterface):
    @router.get("/odom")
    async def get_odom():
        return subscriber.get_latest()

    app.include_router(router)

