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

#---------------------start tugmasi-----------------------------------
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):   
    await message.answer(text="🇺🇿 Kerakli tilni tanlang ! \n 🇷🇺 Выберите язык !", reply_markup=language)

#---------------------salomlashish o'zbekcha-----------------------------------
@dp.callback_query_handler(text=['uz'])
async def uzbekcha(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode='HTML',text=f"Assalomu alaykum hurmatli <b>{call.message.chat.username}</b> ! \n <b>Qarshi muhandislik iqtisodiyot instituti</b> rasmiy botiga hush kelibsiz", reply_markup=uzHeader)

#---------------------salomlashish ruscha-----------------------------------
@dp.callback_query_handler(text=['ru'])
async def ruscha(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode='HTML',text=f"Здраствуйте дорогие {call.message.chat.username} ! \n Добро пожаловать на официальный бот Каршинский Института инженерной экономики", reply_markup=ruHeader)

#-----------------------Bakalavr yo'nalishlari [O'zbekcha yo'nalishlar, Ruscha yo'nalishlar, Belarus fakultetlar]---------------------------------
@dp.callback_query_handler(text='bakalavr')
async def bakalavr(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Kerakli bo'limni tanlang ! 👇", reply_markup=bakalavrUz)
    
    
#-----------------------Rus tilida Bakalavr yo'nalishlari [O'zbekcha yo'nalishlar, Ruscha yo'nalishlar, Belarus fakultetlar]---------------------------------
@dp.callback_query_handler(text='bakalavrRu')
async def bakalavrRu(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Выберите нужный раздел! 👇", reply_markup=bakalavrRu)
    
#-----------------------Bakalavr fakultetlari [Iqtisodiyot, Bank, Moliya ........]---------------------------------
@dp.callback_query_handler(text='uzfak')
async def uzfak(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Kerakli fakultetni tanlang ! 👇", reply_markup=UzFakultetUz)
    
#-----------------------Ruscha Bakalavr fakultetlari [Экономика, Банк, Финанс ........]---------------------------------   
@dp.callback_query_handler(text='rufak')
async def rusfak(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Выберите нужный фaкулътет! 👇", reply_markup=RuFakultetRu)
    

    
@dp.callback_query_handler(text='til')
async def til(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Kerakli tilni tanlang ! \n Выберите язык !", reply_markup=language)
    
    
    
@dp.callback_query_handler(text=['<<UzFak'])
async def uzbekcha(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text=f"Assalomu alaykum hurmatli    <b>{call.message.chat.username}</b> !", reply_markup=uzHeader)
    
    
@dp.callback_query_handler(text=['<<RuFak'])
async def ruscha(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=f"Здраствуйте дорогие {call.message.chat.username} !", reply_markup=ruHeader)
    
    
    
@dp.callback_query_handler(text='<<RuFakRu')
async def bakalavrRu(call:CallbackQuery):
    
    await call.message.delete()
    await call.message.answer(text="📂 Выберите нужный раздел! ! 👇", reply_markup=bakalavrRu)
    
#----------------------------------------------------------------IQTISODIYOT FAKULTETI BARCHA YO'NALISHLARI UZB-----------------------------------------   

@dp.callback_query_handler(text='iqtisod')    
async def iqtisod(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="📂 Fakultetdagi mavjud yo'nalishlar ro'yxati ! \n \n <b>⚫️(5230700) Bank ishi va auditi \n ⚫️(5230900) Buxgalteriya hisobi va audit \n ⚫️(5230100) Iqtisodiyot \n ⚫️(5232501) Logistika \n ⚫️(5230600) Moliya va moliyaviy texnologiyalar \n ⚫️(5230200) Menejment (tarmoqlar va sohalar bo‘yicha)</b>", reply_markup=UzIqtisodUz)


#----------------------------------------------------------------IQTISODIYOT FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text='DekanUzUqtisod')    
async def iqtisod(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Iqtisodiyot fakulteti Dekani: \n 🤵‍♂️Berdiev Abdimalik Hakimovich.\n 📞Bog'lanish: +998907297859 \n 📆Qabul kunlari: Dushanba-Shanba 9:00 – 17:00 \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Hasanov Shamshiddin Xafizovich. \n 📞 Bog'lanish :+998996671529 ! \n 📆Qabul kunlari: Dushanba-Juma kunlari (10:00-17:00) \n \n ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️Mirzayev Komiljon Mamairjonovich. \n  📞Bog'lanish :+998909940787 \n 📆Qabul kunlari: Dushanba-Juma kunlari (10:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzIqtisodDekanat)


#----------------------------------------------------------------NEFT GAZ FAKULTETI NEFT GAZ FAKULTETI UZB-----------------------------------------  


@dp.callback_query_handler(text='neft')    
async def neft(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="📂Neft va Gaz Fakultetdagi mavjud yo'nalishlar ro'yxati ! \n \n ⚫️5311900 – “Neft va gaz konlarini ishga tushirish va ulardan foydalanish”; \n ⚫️5320300 – “Texnologik mashinalar va jihozlar” \n ⚫️5311000 – “Texnologik jarayonlar va ishlab chiqarishni avtomatlashtirish va boshqarish (kimyo, neft-kimyo va oziq-ovqat sanoati)” \n ⚫️5312000 – “Neft-gazni qayta ishlash sanoati obyektlarini loyihalashtirish va qurish” \n ⚫️5321300 – “Neft va neft-gazni qayta ishlash texnologiyasi” \n ⚫️5310900 – “Metrologiya, standartlashtirish va mahsulot sifat menejmenti (sanoat)” ", reply_markup=NeftGazUz)

#----------------------------------------------------------------Neft Gaz FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text="DekanNeftUz")    
async def DekanNeftUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Neft va Gaz fakulteti Dekani: \n 🤵‍♂️Berdiev Abdimalik Hakimovich.\n 📞Bog'lanish: +998907297859 \n 📆Qabul kunlari: Dushanba-Shanba 9:00 – 17:00 \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Hasanov Shamshiddin Xafizovich. \n 📞 Bog'lanish :+998996671529 ! \n 📆Qabul kunlari: Dushanba-Juma kunlari (10:00-17:00) \n \n ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️Mirzayev Komiljon Mamairjonovich. \n  📞Bog'lanish :+998909940787 \n 📆Qabul kunlari: Dushanba-Juma kunlari (10:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzNeftGazDekanat)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
