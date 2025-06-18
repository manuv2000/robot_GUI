from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from interfaces.publisher_interface import RosPublisherInterface

templates = Jinja2Templates(directory="templates")
router = APIRouter()

def register_cmd_vel_routes(app, publisher: RosPublisherInterface):
    @router.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    @router.post("/cmd_vel")
    async def move_robot(linear_x: float = Form(0.0), angular_z: float = Form(0.0)):
        publisher.publish({"linear_x": linear_x, "angular_z": angular_z})
        return RedirectResponse(url="/", status_code=303)

    app.include_router(router)

