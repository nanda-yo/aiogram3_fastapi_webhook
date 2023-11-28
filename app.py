import os
import time
import logging


from fastapi import FastAPI , Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from aiogram import types, Dispatcher, Bot
#from aiogram.types import WebAppInfo
from os import environ
from pydantic import BaseModel


load_dotenv()

bot_Token = os.environ["TG_TOKEN"]
bot_Host = os.environ["VERY_UNIQUE_HOST_NAME"]
bot_WEBHOOK_PATH = f"/bot/{bot_Token}"
bot_WEBHOOK_URL = bot_Host+bot_WEBHOOK_PATH

bot = Bot(token=bot_Token)

dp = Dispatcher(bot=bot)


app = FastAPI(title="meme test api")

## tg bot part

@app.on_event("startup")
async def startup_event():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != bot_WEBHOOK_URL:
        await bot.set_webhook(url=bot_WEBHOOK_URL)


@dp.message()
async def start_handler(message:types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'Start: {user_id} {user_full_name} {time.asctime()}. Message: {message}')
    await message.reply(f"Working, {user_full_name}")

@dp.message()
async def main_handler(message: types.Message):
    try:
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        logging.info(f'Main: {user_id} {user_full_name} {time.asctime()}. Message: {message}')
        await message.reply("Hello world!")
    except:
        logging.info(f'Main: {user_id} {user_full_name} {time.asctime()}. Message: {message}. Error in main_handler')
        await message.reply("Something went wrong...")


@app.post(bot_WEBHOOK_PATH)
async def bot_webhook(update: dict):
    tg_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(tg_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.get_session().close()



api_app = FastAPI(title="api app")
app.mount("/api",api_app)




class Item(BaseModel):
    item_id: int


@app.get("/meow/")
async def root():
    return {"message": "Hello World HEH"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
async def list_items():
    return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


@app.post("/items/")
async def create_item(item: Item):
    return item


app.mount("/",StaticFiles(directory="gui",html=True),name="gui")
