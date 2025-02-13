import logging
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
import os

# Импортируем FastAPI сервер
from backend.main import app as fastapi_app
from uvicorn import run
import threading

TOKEN = os.environ.get("BOT_TOKEN") #7853194280:AAEmg22Kgv-Pj328MFx6BRHk2ZyhkkzfGSc
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    # Создаём клавиатуру с кнопкой для открытия кликера
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Открыть кликер", web_app=WebAppInfo(url="https://your-server.com"))]],
        resize_keyboard=True
    )
    await message.answer("Нажми на кнопку, чтобы открыть кликер!", reply_markup=keyboard)

dp.include_router(router)

# Запуск FastAPI на отдельном потоке
def start_fastapi():
    run(fastapi_app, host="0.0.0.0", port=8000)

# Запуск бота с aiogram 3.x
async def start_bot():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запуск FastAPI на отдельном потоке
    fastapi_thread = threading.Thread(target=start_fastapi, daemon=True)
    fastapi_thread.start()

    # Запуск бота
    asyncio.run(start_bot())
