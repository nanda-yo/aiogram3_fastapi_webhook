from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.types import WebhookInfo, BotCommand

from bot.settings import get_settings, Settings

config:Settings = get_settings()

tg_router = Router(name="test")
dp = Dispatcher()

dp.include_router(tg_router)
bot = Bot(token=config.bot_token, parse_mode=ParseMode.HTML)

async def set_webhook(the_bot: Bot) -> None:
    async def check_webhook() -> WebhookInfo | None:
        try:
            webhook_info = await the_bot.get_webhook_info()
            return webhook_info
        except Exception as error:
            print(f"Cannot get webhook  - {error}")
            return
    current_webhook_info = await check_webhook()
    if config.debug:
        print(f"WEBHOOKINFO :: => {current_webhook_info}")
    try:
        await bot.set_webhook(

            f"{config.webhook_url}{config.webhook_path}",
            secret_token=config.secret_tg_token,
            drop_pending_updates=current_webhook_info.pending_update_count>0,
            max_connections=3 if config.debug else 10
        )
    except Exception as error:
        print(f"Cannot set webhook => {error}")


async def start_bot():
    print(f"setting webhook")
    await set_webhook(bot)
