from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from backend.api import apirouter
from frontend.control import front


app = FastAPI(title="Nettify Meeting Connect")
front.mount("/static", StaticFiles(directory="frontend/static"), name="static")

templates = Jinja2Templates(directory="frontend/templates",)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(apirouter)
app.include_router(front)

data = {"List": [
        {"img":"http://castcdn.nettify.com/beef-burger.jpg", "timer":20, "hideWelcomme": False, "useVideo": False},
        {"img":"http://castcdn.nettify.com/nettify-explainer.mp4", "timer":0, "hideWelcomme": False, "useVideo": True},
        {"img":"http://castcdn.nettify.com/Restaurant_promo_03.jpg", "timer":20, "hideWelcomme": False, "useVideo": False},
        {"img":"http://castcdn.nettify.com/NettifyCast-latest.mp4", "timer":0, "hideWelcomme": False, "useVideo": True},
        {"img":"http://castcdn.nettify.com/spa-night.jpg", "timer":20, "hideWelcomme": False, "useVideo": False}
        ],
     "Type": "bannerlist",
     "app.version": "1.0.0.0" }
