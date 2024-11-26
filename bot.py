from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

TOKEN = "ВАШ_ТОКЕН"
WEB_APP_URL = "https://ВАШ_ДОМЕН"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    # Создаем кнопку для открытия мини-приложения
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="Открыть мини-приложение",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    )
    await message.answer("Привет! Нажми на кнопку, чтобы открыть мини-приложение.", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
