from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from .browser import browser
from jinja2 import Template
import logging
from .models import BannerList, BasicConfig, MeetingConfig, OkResponse


apirouter = APIRouter(prefix="/api", tags=["backend"])
templates = Jinja2Templates(directory='frontend/templates')


@apirouter.get("/startMeeting", response_class=HTMLResponse)
async def start_meeting(request: Request):
    return templates.TemplateResponse("lobby.html", {"request": request})


@apirouter.post("/startMeeting", response_class=HTMLResponse)
async def host_meeting(request: Request, data: MeetingConfig):
    with open('frontend/templates/meet.html') as t:
        templ = Template(t.read())

    templ.stream(
        room_name=data.meetingRoomName,
        displayName=data.displayName,
        email=data.email
        ).dump("frontend/static/meet.html")
    browser.execute_script("location.href='http://localhost:8000/static/meet.html'")
    
    return templates.TemplateResponse("control.html", {"request": request})


@apirouter.post("/setPassword", response_model=OkResponse)
async def meeting_config(config: BasicConfig):
    passwd = config.password
    lobby = str(config.lobby).lower()
    browser.execute_script(f"return api.executeCommand('toggleLobby', {lobby});")
    browser.execute_script(f"return api.executeCommand('password', '{passwd}');")
    resp = {
        "status": "Ok"
    }
    return resp


#TODO: Fix browser console execution
@apirouter.post("/bannerList", response_model=OkResponse)
async def set_bannet_list(bannerList: BannerList):
    browser.execute_script(f"var bannerList = {bannerList}")
    logging.info("List are {}", bannerList)
    resp = {
        "status": "Banner list updated"
    }
    return resp


@apirouter.get("/bannerList", response_model=BannerList)
async def get_banner_list():
    resp = browser.execute_script("return bannerList")
    return resp


@apirouter.get("/playDefBanner")
async def serve_def_banner():
    data = {"List": [
        {"img":"http://castcdn.nettify.com/beef-burger.jpg", "timer":20, "hideWelcomme": False, "useVideo": False},
        {"img":"http://castcdn.nettify.com/nettify-explainer.mp4", "timer":0, "hideWelcomme": False, "useVideo": True},
        {"img":"http://castcdn.nettify.com/Restaurant_promo_03.jpg", "timer":20, "hideWelcomme": False, "useVideo": False},
        {"img":"http://castcdn.nettify.com/NettifyCast-latest.mp4", "timer":0, "hideWelcomme": False, "useVideo": True},
        {"img":"http://castcdn.nettify.com/spa-night.jpg", "timer":20, "hideWelcomme": False, "useVideo": False}
        ],
     "Type": "bannerlist",
     "app.version": "1.0.0.0" }
    return data