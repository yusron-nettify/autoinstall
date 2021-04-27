from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ..main import templates


front = APIRouter(tags=["control"])

@front.get("/control", response_class=HTMLResponse)
async def get_control(request: Request):
    return templates.TemplateResponse("control.html", {"request": request})


@front.get("/receiver", response_class=HTMLResponse)
async def get_receiver(request: Request):
    return templates.TemplateResponse("receiver.j2", {"request": request})