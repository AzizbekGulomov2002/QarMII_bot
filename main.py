"""
This is a echo bot.
It echoes any incoming text messages.
"""

from html.entities import html5
import logging
from pydoc import html, text
from config import *
from buttons import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print(message)
    bot.delete_message()
    await message.answer(text="🇺🇿 Kerakli tilni tanlang ! \n 🇷🇺 Выберите язык !", reply_markup=language)


@dp.callback_query_handler(text=['uz'])
async def uzbekcha(call:CallbackQuery):
    bot.delete_message()
    await call.message.answer(parse_mode='HTML',text=f"Assalomu alaykum hurmatli <b>{call.message.chat.username}</b> ! \n <b>Qarshi muhandislik iqtisodiyot instituti</b> rasmiy botiga hush kelibsiz", reply_markup=uzHeader)


@dp.callback_query_handler(text=['ru'])
async def ruscha(call:CallbackQuery):
    
    await call.message.answer(parse_mode='HTML',text=f"Здраствуйте дорогие {call.message.chat.username} ! \n Добро пожаловать на официальный бот Каршинский Института инженерной экономики", reply_markup=ruHeader)


@dp.callback_query_handler(text='bakalavr')
async def bakalavr(call:CallbackQuery):
    #reply - ayni bir habarga javob
    await call.message.answer(text="📂 Kerakli bo'limni tanlang ! 👇", reply_markup=bakalavrUz)
    
    

@dp.callback_query_handler(text='bakalavrRu')
async def bakalavrRu(call:CallbackQuery):
    #reply - ayni bir habarga javob
    await call.message.answer(text="📂 Выберите нужный раздел! 👇", reply_markup=bakalavrRu)
    
    
@dp.callback_query_handler(text='uzfak')
async def uzfak(call:CallbackQuery):
    #reply - ayni bir habarga javob
    await call.message.answer(text="📂 Kerakli fakultetni tanlang ! 👇", reply_markup=UzFakultetUz)
    
    
@dp.callback_query_handler(text='rufak')
async def rusfak(call:CallbackQuery):
    #reply - ayni bir habarga javob
    await call.message.answer(text="📂 Выберите нужный фaкулътет! 👇", reply_markup=RuFakultetRu)
    

    
@dp.callback_query_handler(text='til')
async def til(call:CallbackQuery):
    await call.message.answer(text="Kerakli tilni tanlang ! \n Выберите язык !", reply_markup=language)
    
    
    
@dp.callback_query_handler(text=['<<UzFak'])
async def uzbekcha(call:CallbackQuery):
    
    await call.message.answer(text=f"Assalomu alaykum hurmatli {call.message.chat.username} !", reply_markup=uzHeader)
    
    
@dp.callback_query_handler(text=['<<RuFak'])
async def ruscha(call:CallbackQuery):
    
    await call.message.answer(text=f"Здраствуйте дорогие {call.message.chat.username} !", reply_markup=ruHeader)
    
    
    
@dp.callback_query_handler(text='<<UzFakUz')
async def bakalavr(call:CallbackQuery):
    #reply - ayni bir habarga javob
    await call.message.answer(text="📂 Kerakli bo'limni tanlang ! 👇", reply_markup=bakalavrUz)
    
    
    
    
@dp.callback_query_handler(text='<<RuFakRu')
async def bakalavrRu(call:CallbackQuery):
    
    #reply - ayni bir habarga javob
    await call.message.answer(text="📂 Выберите нужный раздел! ! 👇", reply_markup=bakalavrRu)
    
    

@dp.callback_query_handler(text='iqtisod')    
async def iqtisod(call:CallbackQuery):
    await call.message.answer(text="📂 Kerakli yo'nalishlar ro'yxati ! 👇", reply_markup=UzIqtisodUz)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
