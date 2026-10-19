from aiogram import Bot, Dispatcher
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message):
    await message.answer("Привет из aiogram!")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())