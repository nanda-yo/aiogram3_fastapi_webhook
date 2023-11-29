from typing import Annotated
from fastapi import APIRouter, Header
from aiogram import types
from bot.bot import dp,bot
from bot.settings import get_settings

config = get_settings()

tg_bot_router = APIRouter()

@tg_bot_router.post(f"{config.webhook_path}")
async def bot_webhook(update:dict,received_x_tg_token: Annotated[str|None,Header()] = None) -> None | dict:
    if received_x_tg_token != config.secret_tg_token:
        print(f" Secret token doesnt match")
        return {f"Token mismatch, error."}
    telegram_update = types.Update(**update)
    await dp.feed_webhook_update(bot=bot,update=telegram_update)
