import asyncio
from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN
from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.registration import router as registration_router

dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(registration_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())
