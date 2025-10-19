import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import asyncio

# Загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот для недвижимости SAV.\n\n"
        "Я могу искать квартиры, аренду, участки и дома по Испании.\n"
        "Напиши, что тебя интересует, например:\n\n"
        "<b>аренда Бенидорм 2 спальни до 1300€</b>"
    )

async def main():
    print('Бот запущен ✅')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
