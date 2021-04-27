from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
# from .browser import browser
from jinja2 import Template
import logging
from .models import BannerList, BasicConfig, MeetingConfig, OkResponse


apirouter = APIRouter(prefix="/api", tags=["backend"])
webdir ='/opt/nettify/meet/jitsi-meet/src/web/templates/'
templates = Jinja2Templates(directory=webdir)


@apirouter.get("/starMeeting", response_class=HTMLResponse)
async def start_meeting(request: Request):
    return templates.TemplateResponse("lobby.html", {"request": request})


@apirouter.post("/startMeeting", response_class=HTMLResponse)
async def host_meeting(request: Request, data: MeetingConfig):
    with open(webdir + 'meeting.j2') as t:
        templ = Template(t.read())

    templ.stream(
        room_name=data.meetingRoomName,
        displayName=data.displayName,
        email=data.email
        ).dump("/opt/nettify/meet/jitsi-meet/src/web/jitsi/meet.html")
    browser.execute_script("location.href='http://localhost/jitsi/meet.html'")
    
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