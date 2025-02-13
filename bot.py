import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command

TOKEN = "7853194280:AAEmg22Kgv-Pj328MFx6BRHk2ZyhkkzfGSc"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text="Открыть кликер", web_app=WebAppInfo(url="https://your-yhub-project.yhub.net"))
    keyboard.add(button)
    await message.answer("Нажми на кнопку, чтобы открыть кликер!", reply_markup=keyboard)

dp.include_router(router)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
