# bot.py

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.client.default import DefaultBotProperties  # ← ДОБАВЛЕНО
import asyncio

from config import TOKEN, PROMO, OFFER_LINK

# ← ОБНОВЛЁННЫЙ способ задания parse_mode
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)


def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎁 Получить промо")],
            [KeyboardButton(text="📖 Инструкция"), KeyboardButton(text="💬 Отзывы")],
            [KeyboardButton(text="🌍 Сменить язык")]
        ],
        resize_keyboard=True
    )

@router.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("Привет! Добро пожаловать в бонус-бот 🎰", reply_markup=get_main_keyboard())

@router.message(F.text == "🎁 Получить промо")
async def promo_handler(message: Message):
    await message.answer(f"<b>🎁 Твой промокод:</b> <code>{PROMO}</code>\n\nПерейди по ссылке: {OFFER_LINK}")

@router.message(F.text == "📖 Инструкция")
async def instruction_handler(message: Message):
    await message.answer("1. Жми 'Получить промо'\n2. Переходи по ссылке\n3. Вводи промокод и получай бонус!")

@router.message(F.text == "💬 Отзывы")
async def reviews_handler(message: Message):
    await message.answer("💬 Иван: Выиграл 500₽!\n💬 Марина: Бот реально работает!")

@router.message(F.text == "🌍 Сменить язык")
async def language_handler(message: Message):
    await message.answer("Пока доступен только русский 🌍\nСкоро добавим английский!")

@router.message()
async def unknown_handler(message: Message):
    await message.answer("Пожалуйста, выбери действие с клавиатуры 👇")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
