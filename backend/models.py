from pydantic import BaseModel
from typing import List

class BasicConfig(BaseModel):
    password: str
    lobby: bool

class OkResponse(BaseModel):
    status: str

class Banner(BaseModel):
    img: str
    timer: int
    hideWelcomme: bool
    useVideo: bool

class BannerList(BaseModel):
    list: List[Banner]

class MeetingConfig(BaseModel):
    meetingRoomName: str
    displayName: str
    email: str