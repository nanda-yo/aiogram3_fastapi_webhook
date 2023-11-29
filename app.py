from fastapi import FastAPI
from contextlib import asynccontextmanager
from handlers import messages
from bot.settings import get_settings
from routers.api import api_app
from routers.bot_route import tg_bot_router
from fastapi.staticfiles import StaticFiles

config = get_settings()



@asynccontextmanager
async def lifespan(application: FastAPI):
    print(f"Starting app")
    from bot.bot import start_bot
    await start_bot()
    yield
    print(f"Quitting")

#fastapi handler
app = FastAPI(title="meme test api", lifespan=lifespan)
app.include_router(api_app)
app.include_router(tg_bot_router)
app.mount("/",StaticFiles(directory="gui",html=True),name="gui")
