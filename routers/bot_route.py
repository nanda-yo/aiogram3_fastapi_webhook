from typing import Annotated
from fastapi import APIRouter, Header, HTTPException, Response
from aiogram import types
from bot.bot import dp,bot
from bot.settings import get_settings

config = get_settings()

tg_bot_router = APIRouter()

@tg_bot_router.post(config.webhook_path,include_in_schema=False)
async def bot_webhook(update: dict,
                      x_telegram_bot_api_secret_token: Annotated[str | None, Header()] = None) -> None | dict:
    if x_telegram_bot_api_secret_token != config.secret_tg_token:
        print(f" Secret token doesnt match")
        return {"status": "Token mismatch", "message": f"Expected => {config.secret_tg_token}, /n Received : {x_telegram_bot_api_secret_token}!"}
    telegram_update = types.Update(**update)
    await dp.feed_webhook_update(bot=bot,update=telegram_update)
@tg_bot_router.post("/sendMessageForm")
async def sendPlainMessageForm(name:str,text:str,captcha:bool):
    if captcha:
        #return {"Name": name,"text":text}
        await bot.send_message(config.user_id, (f"Name: {name}\nText: {text}"))
        return Response(status_code=200)
    else:
        raise HTTPException(status_code=409,detail="Wrong captcha",headers={"X-error": "Captcha mismatch"})
        return captcha