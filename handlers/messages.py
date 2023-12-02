import bot.bot
from aiogram import types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from aiogram.methods import SendMessage

from bot.bot import tg_router

@tg_router.message(CommandStart())
async def bot_cmd_start(message: Message) -> None:
    await message.answer(f"Hi, start command is working.")

@tg_router.message(Command("UserData"))
async def bot_cmd_user_data(message:Message) -> None:
    await message.answer(f"Your ID is : {message.from_user.id} and your full name is : {message.from_user.full_name}")

