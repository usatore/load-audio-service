from fastapi import FastAPI
from app.audiofiles.router import router as router_audiofiles


app = FastAPI()

app.include_router(router_audiofiles)


