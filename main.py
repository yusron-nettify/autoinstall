from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from backend.api import apirouter
from frontend.control import front
import uvicorn

app = FastAPI(title="Nettify Meeting Connect")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(front)
app.include_router(apirouter)

if __name__=="__main__":
    uvicorn.run(app)