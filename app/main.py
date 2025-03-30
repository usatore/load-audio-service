from fastapi import FastAPI
from app.audiofiles.router import router as router_audiofiles
from app.users.router import router as router_users


app = FastAPI()

app.include_router(router_audiofiles)
app.include_router(router_users)


