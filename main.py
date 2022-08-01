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
    await message.answer(parse_mode='HTML',text=f"Assalomu alaykum hurmatli <b>{message.chat.username}</b> ! \n <b>Qarshi muhandislik iqtisodiyot instituti</b> rasmiy botiga hush kelibsiz", reply_markup=uzHeader)


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
    await call.message.answer(parse_mode="HTML",text=f"Assalomu alaykum hurmatli    <b>{call.message.chat.username}</b> ! \n ASOSIY BO'LIM", reply_markup=uzHeader) 
    
    
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


#-----------------------------------IQTISODIYOT FAKULTETI DEKANATIGA MUROJAAT-----------
@dp.callback_query_handler(text='UzIqtisodDekanat')
async def UzIqtisodDekanat(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Iqtisodiyot dekanatiga murojaat : .... \n Namunadagi kabi yo'llang !")
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    

@dp.callback_query_handler(text='DekanUzIqtisod')    
async def iqtisod(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Iqtisodiyot fakulteti Dekani: \n 🤵‍♂️Berdiev Abdimalik Hakimovich.\n 📞Bog'lanish: +998907297859 \n 📆Qabul kunlari: Dushanba-Shanba 9:00 – 17:00 \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Hasanov Shamshiddin Xafizovich. \n 📞 Bog'lanish :+998996671529 ! \n 📆Qabul kunlari: Dushanba-Juma kunlari (10:00-17:00) \n \n ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️Mirzayev Komiljon Mamairjonovich. \n  📞Bog'lanish :+998909940787 \n 📆Qabul kunlari: Dushanba-Juma kunlari (10:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=IqtisodDekanat)


#----------------------------------------------------------------NEFT GAZ FAKULTETI NEFT GAZ FAKULTETI UZB-----------------------------------------  


@dp.callback_query_handler(text='neft')    
async def neft(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="📂Neft va Gaz Fakultetdagi mavjud yo'nalishlar ro'yxati ! \n \n ⚫️5311900 – “Neft va gaz konlarini ishga tushirish va ulardan foydalanish”; \n ⚫️5320300 – “Texnologik mashinalar va jihozlar” \n ⚫️5311000 – “Texnologik jarayonlar va ishlab chiqarishni avtomatlashtirish va boshqarish (kimyo, neft-kimyo va oziq-ovqat sanoati)” \n ⚫️5312000 – “Neft-gazni qayta ishlash sanoati obyektlarini loyihalashtirish va qurish” \n ⚫️5321300 – “Neft va neft-gazni qayta ishlash texnologiyasi” \n ⚫️5310900 – “Metrologiya, standartlashtirish va mahsulot sifat menejmenti (sanoat)” ", reply_markup=NeftGazUz)

#----------------------------------------------------------------Neft Gaz FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text="DekanNeftUz")    
async def DekanNeftUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Neft va Gaz fakulteti Dekani: \n 🤵‍♂️Raxmatov Erkin Аbdihafizovich.\n 📞Bog'lanish: +998999459812 \n 📆Qabul kunlari: Dushanba-Juma kunlari (15:00-17:00) \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Nurqulov Eldor Nurmuminovich. \n 📞 Bog'lanish : +998995300225 ! \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Abdirazakov Akmal Ibragimovich. \n 📞 Bog'lanish : +998907228015 ! \n 📆Qabul kunlari:  Dushanba-Juma kunlari (15:00-17:00) \n \n ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️Sharipov G‘ulomjon Qarshi о‘g‘li. \n  📞Bog'lanish :+998905185333 \n 📆Qabul kunlari: Dushanba-Juma kunlari (10:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzNeftGazDekanat)



#----------------------------------------------------------------ENERGETIKA FAKULTETI NEFT GAZ FAKULTETI UZB-----------------------------------------  


@dp.callback_query_handler(text='energetika')    
async def energetika(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="📂Energetika Fakultetdagi mavjud yo'nalishlar ro'yxati ! \n \n ⚫️5310100-Energetika (issiqlik energetikasi); \n ⚫️5310200 – Elektr energetikasi (elektr ta’minoti); \n ⚫️5312400-Muqobil energiya manbalari (turlari bo’yicha); \n ⚫️5A310104-Sanoat issiqlik energetikasi; \n ⚫️55A310204-Elektr energetikasi tizimlari va tarmoqlari (faoliyat turlari bo‘yicha); ", reply_markup=EnergiyaUz)


#----------------------------------------------------------------ENERGETIKA FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text="DekanEnergiyaUz")    
async def DekanEnergiyaUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Energetika fakulteti Dekani: \n 🤵‍♂️Sa’dullayev Aloviddin Bobaqulovich. \n 📞Bog'lanish:  +998939013324 \n 📆Qabul kunlari: Dushanba-Payshanba kunlari (15:00-17:00) \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Abdinazarov Sarvar Burxonovich. \n 📞 Bog'lanish : +99897374103 ! \n  ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️Abdullayev O‘ktamjon Sheraliyevich. \n  📞Bog'lanish :+998914119570 \n 📆Dushanba-Juma kunlari (10:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzEnergiyaDekanat)


#----------------------------------------------------------------Sanoat texnologiyalari FAKULTETI NEFT GAZ FAKULTETI UZB-----------------------------------------  


@dp.callback_query_handler(text='sanoat')    
async def sanoat(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="Sanoat texnologiyalari Fakultetdagi mavjud yo'nalishlar ro'yxati ! \n \n ⚫️5320400 – Kimyoviy texnologiya (ishlab chiqarish turlari bo'yicha); \n ⚫️5321000 – Oziq-ovqat texnologiyasi (mahsulot turlari bo'yicha); \n ⚫️5311000 – Texnologik jarayonlar va ishlab chiqarishni avtomatlashtirish  va boshqarish (tarmoqlar bo'yicha); \n ⚫️5310900 – Metrologiya, standartlashtirish va mahsulot sifati menejmenti (tarmoqlar bo'yicha); \n ⚫️5310800 – Elektronika va asbobsozlik (tarmoqlar bo'yicha); \n 5410500 – Qishloq xo'jalik mahsulotlarini saqlash va dastlabki ishlash texnologiyasi (mahsulotlar turlari bo'yicha); ", reply_markup=SanoatUz)


#----------------------------------------------------------------SANOAT FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text="DekanSanoatUz")    
async def DekanSanoatUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Energetika fakulteti Dekani: \n 🤵‍♂️Panjiyev Ulug'bek Rustamovich. \n 📞Bog'lanish:  +998904268393 \n 📆Dushanba-Payshanba kunlari (15:00-17:00) \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Nazarov Asror Allanazarovich. \n 📞 Bog'lanish : +998904278304 ! \n 📆Dushanba-Juma kunlari (10:00-17:00) \n \n  ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️Davlatov Farrux Farxodovich. \n  📞Bog'lanish :+998912236944 \n 📆Dushanba-Juma kunlari (10:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzSanoatDekanat)


#----------------------------------------------------------------Geologiya va konchilik FAKULTETI NEFT GAZ FAKULTETI UZB-----------------------------------------  


@dp.callback_query_handler(text='geologiya')    
async def geologiya(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="Geologiya va konchilik Fakultetdagi mavjud yo'nalishlar ro'yxati ! \n \n ⚫️5311700 -“Foydali qazilmalar geologiyasi va razvedkasi”; \n ⚫️5311600-“Konchilik ishi” \n ⚫️5630100- “ Ekologiya va mehnat muhofazasi” \n ⚫️5410700- “Geodeziya kadastr va erdan foydalanish”  ", reply_markup=GeologiyaUz)


#----------------------------------------------------------------Geologiya va konchilik FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text="DekanGeologiyaUz")    
async def DekanGeologiyaUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Geologiya va konchilik fakulteti Dekani: \n 🤵‍♂️Yarboboev To‘lqin Nurboboevich. \n 📞Bog'lanish:  +998919560506 \n 📆Dushanba-Payshanba kunlari (15:00-17:00) \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Zuxurov Yigitali Tog‘ayevich. \n 📞 Bog'lanish : +998934232111 ! \n 📆Dushanba-Juma kunlari (10:00-17:00) \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Sultonov Shuxrat Adxamovich. \n 📞 Bog'lanish : +998930710787 ! \n 📆Dushanba-Juma kunlari (10:00-17:00) \n \n  ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️Sultonov Shuxrat Adxamovich. \n  📞Bog'lanish :+998930710787 \n 📆Dushanba-Juma kunlari (10:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzSanoatDekanat)



#----------------------------------------------------------------Muhandislik texnikasi FAKULTETI UZB-----------------------------------------  


@dp.callback_query_handler(text='muhandislik')    
async def muhandislik(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="Muhandislik Fakultetdagi mavjud yo'nalishlar ro'yxati !   ", reply_markup=GeologiyaUz)


#----------------------------------------------------------------Muhandislik FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text="DekanMuhandisUz")    
async def DekanMuhandisUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Muhandislik texnikasi fakulteti Dekani: \n 🤵‍♂️Chuyanov Dustmurod Shodmonovich. \n 📞Bog'lanish:  +998912148338 \n 📆Dushanba-Shanba (9:00-17:00) \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Toshtemirov Sanjar Jumaniyazovich. \n 📞 Bog'lanish : +998907290709 ! \n 📆Dushanba-Juma kunlari (10:00-17:00) \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Latipov Shahboz Alisher o‘g‘li. \n 📞 Bog'lanish : +998914601222 ! \n 📆Seshanba-Payshanba kunlari (09:00-17:00) \n \n  ⚫️Yoshlar bilan ishlash bo’yicha dekan o'rinbosari: \n 🤵‍♂️To’rayev O’lmas Sanoqulovich. \n  📞Bog'lanish :+998916357535 \n 📆Dushanba-Juma kunlari (15:00-17:00) \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzMuhandisDekanat)

#----------------------------------------------------------------Elektronika va avtomatika FAKULTETI UZB-----------------------------------------  


@dp.callback_query_handler(text='elektroAvto')    
async def elektroAvto(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="Elektronika va avtomatika Fakultetdagi mavjud yo'nalishlar ro'yxati ! \n \n ⚫️“Texnologik jarayonlarni avtomatlashtirish va boshqaruv” \n ⚫️“Fizika va elektronika” \n ⚫️“Axborot texnologiyalari” \n ⚫️“Oliy matematika”  ", reply_markup=ElektroAvtoUz)


#----------------------------------------------------------------Elektronika va avtomatika FAKULTETI DEKANATI  UZB-----------------------------------------  

@dp.callback_query_handler(text="ElektroavtoDekanat")    
async def ElektroavtoDekanat(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="📂 Elektronika va avtomatika fakulteti Dekani: \n 🤵‍♂️Mallayev Alisher Rajabaliyevich. \n 📞Bog'lanish:  +998946149249 \n 📆Qabul kunlari: Dushanba-Payshanba kunlari (15:00-17:00) \n \n ⚫️O'quv ishlari bo'yicha Dekan o'rinbosari: \n 🤵‍♂️Rajabov Jamshid Nasrillayevich. \n 📞 Bog'lanish :  +998972293094 \n 📆Dushanba-Juma kunlari (10:00-17:00) \n  \n \n  ☎️Kall markaz: +998752200924", reply_markup=UzElektroAvtoDekanat)


#----------------------------------------------------------------UNIVERSITET HAQIDA MALUMOT-----------------------------------------  
@dp.callback_query_handler(text='haqida')    
async def haqida(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="<b>Qarshi muhandislik-iqtisodiyot instituti</b> — Iqtisodchi, qishloq xoʻjaligi, neft va gaz sanoati, elektr va issiqlik energetikasi, oziqovqat sanoati, kimyoviy texnologiya va xalq xoʻjaligining boshqa tarmoqlari hamda taʼlim sohasi uchun yuqori malakali muhandislar, iqtisodchi va muhandispedagog bakalavrlar va mutaxassislar tayyorlaydigan oliy oʻquv yurti. U Toshkent irrigatsiya va melioratsiya institutining Qarshi filiali negizida 1992-yilda tashkil etilgan. Institutda 28 ta taʼlim yoʻnalishi boʻyicha bakalavrlar, 12 ta mutaxassislik boʻyicha magistrlar va doktaranturada 7 ixtisoslik boʻyicha ilmiypedagogik xodimlar tayyorlanadi. Institutda qishloq xoʻjaligi ishlab chiqarishini mexanizatsiyalash, xalq xoʻjiligi iqtisodiyoti, agronomiya, neft va gaz ishi, elektrotexnologiya sohalari boʻyicha ilmiy tekshirish ishlari olib boriladi. institut qoshida litseyinternat, akademik litsey, biznes maktablari, mutaxassislar malakasini oshirish boʻlimi, Iqtidorli talabalar bilan ishlash, Axborot texnologiyalari va masofaviy taʼlim markazlari, kichik bosmaxona faoliyat koʻrsatadi. Institutda 31 ta kafedra, kutubxona 230 mingdan ortiq kitoblar mavjud. Institut tashkil etilgandan buyon 18 mingdan ortiq yuqori malakali mutaxassis va bakalavrlar tayyorlandi. institut Rossiya, AQSH, Germaniya, Turkiya, Latviya, Gretsiya, Litva, Portugaliya, Ruminiya, Polsha va boshqalar mamlakatlarning oliy oʻquv yurtlari bilan hamkorlik qiladi. Xususan; Belorusiya Davlat Texnika Universiteti, Ispaniyadagi La Laguna universiteti va boshqalar. Institutda talabalarning dam olish oromgohi, sogʻlomlashtirish markazi, sport saroyi mavjud. \n \n \n Qarshi muhandislik iqtisodiyot instituti Web platformasi: \n https://qmii.uz ", reply_markup=UniverHaqidaUz)

#----------------------------------------------------------------REKTORAT HAQIDA-----------------------------------------  

@dp.callback_query_handler(text='rektoratUz')    
async def rektoratUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ Qarshi muhandislik-iqtisodiyot instituti Rektori \n <b>Bazarov Orifjan Shadiyevich</b> \n 📆Qabul kunlari \n Seshanba (9:00-17:00), Juma (9:00-17:00): \n Qabulxona: +998752210923 \n \n ⚫️ Qarshi muhandislik-iqtisodiyot instituti yoshlar bilan ishlash bo'yicha Prorektor: \n <b> Xayriddinov Azamat Botirovich </b> \n 📆Qabul kunlari \n Dushanba (9:00-17:00),Payshanba (9:00-17:00): \n Qabulxona: +998752211708 \n \n ⚫️ Qarshi muhandislik-iqtisodiyot instituti o'quv ishlari bo'yicha Prorektor: <b> Bozorov Otabek Nashvandovich </b> \n 📆Qabul kunlari \n Chorshanba (9:00-17:00), Payshanba (9:00-17:00): \n Qabulxona: +998752211127 \n \n ⚫️ Qarshi muhandislik-iqtisodiyot instituti ilmiy ishlar va innovatsiyalar bo'yicha Prorektor: \n <b> Uzoqov G`ulom Norboyevich </b> \n 📆Qabul kunlari \n Chorshanba (9:00–17:00), Shanba (9:00-17:00): \n Qabulxona: +998752240289 \n \n ⚫️ Qarshi muhandislik-iqtisodiyot instituti moliya va iqtisodiyot bo'yicha Prorektor: \n <b> Mamatov Suxrab Farmonovich </b> \n 📆Qabul kunlari \n  Dushanba (15:00–17:00), Shanba(9:00-17:00): \n ☎️Qabulxona: +998752241396", reply_markup=RektoratUz)


#----------------------------------------------------------------MAGISTRATURA-----------------------------------------  

@dp.callback_query_handler(text='magistrUz')    
async def magistrUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Qarshi muhandislik-iqtisodiyot instituti Magistratura yo'nalishlari</b>: \n \n <b>5A630101 - Atrof-muhit muhofazasi (tarmoqlar va sohalar boʻyicha) \n 5A230902 - Audit (tarmoqlar va sohalar boʻyicha) \n 5A230901 - Buxgalteriya hisobi (tarmoqlar va sohalar boʻyicha) \n 5A230601 - Davlat moliyasi va xalqaro moliya \n 5A310204 - Elektr energetikasi tizimlari va tarmoqlari (faoliyat turlari boʻyicha) \n 5A311601 - Foydali qazilma konlarini qazish (qazish usullari boʻyicha) \n 5A141104 - Gidravlika va muhandislik gidrologiyasi \n 5A340703 - Gidroelektr va nasos stansiyalari qurilishi \n 5A310101 - Gidroelektrstansiyalar \n 5A340701 - Gidrotexnika inshootlari (inshootlar turi boʻyicha) \n 5A230102 - Iqtisodiyot (tarmoqlar va sohalar boʻyicha) \n 5A311301 - Kadastr (faoliyat turlari boʻyicha) \n 5A320401 - Kimyoviy texnologiya (ishlab chiqarish turlari boʻyicha) \n 5A640101 - Mehnat muhofazasi, ishlab chiqarish va texnologik jarayonlar xavfsizligi (tarmoqlar boʻyicha) \n 5A230201 - Menejment (tarmoqlar va sohalar boʻyicha) \n 5A232301 - Mintaqaviy iqtisodiyot \n 5A312401 - Muqobil energiya manbalari (turlari boʻyicha) \n 5A311902 - Neft va gaz konlari mashina va jihozlaridan foydalanish \n 5A311901 - Neft va gaz konlarini ishga tushirish va ulardan foydalanish \n 5A311903 - Neft va gaz quduqlarini burgʻulash \n 5A321303 - Neft va gazni qayta ishlash jarayonlari va apparatlari \n 5A321302 - Neft va gazni qayta ishlash va kimyoviy texnologiyasi \n 5A321101 - Oziq-ovqat mahsulotlarini ishlab chiqarish va qayta ishlash texnologiyasi (mahsulot turlari boʻyicha) \n 5A410501 - Qishloq xoʻjalik mahsulotlarini saqlash va dastlabki ishlash texnologiyasi (mahsulotlar turlari boʻyicha) \n 5A310104 - Sanoat issiqlik energetikasi \n 5A310601 - Yer usti transport vositalari va tizimlari (transport turlari boʻyicha) \n 5A320405 - Yuqori molekulali birikmalar kimyoviy texnologiyasi (turlari boʻyicha)</b> \n \n ☎️Qabulxona: +998752210923", reply_markup=MagistrUz)


#----------------------------------------------------------------KAFEDRALAR-----------------------------------------  

@dp.callback_query_handler(text="kafedraUz")    
async def kafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Ushbu bo'limda institut kafedralari ro'yxati shakillantirilgan</b> : \n \n", reply_markup=KafedraUz)


#----------------------------------------------------------------KANTRAKT BUJETLAR-----------------------------------------  

@dp.callback_query_handler(text="kontrakUz")    
async def kontrakuz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Kontrakt summalari</b> :  2022-yil hisobiga ko'ra:\n \n Stipendiyalik kontrakt : <b>14,264,000 so'm</b> \n Stipendiyasiz kontrakt : <b>7,264,000</b> so'm \n \n Sipendiya summasi (o'rta baho): <b>564,000 so'm </b> \n Stipendiya summasi (a'lo baho): <b>634,000 so'm </b>", reply_markup=KantrakBujetUz)

#----------------------------------------------------------------STATISTIKA----------------------------------------  

@dp.callback_query_handler(text="statistikaUz")    
async def statistikaUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Telegram bot foydalanuvchilasi soni : 1,999,999 ta \n Kunlik foydalanuvchilar soni: 2,099 ta</b> ", reply_markup=StatistikaUz)



#----------------------------------------------------------------YANGILIKLAR IT KURSLAR----------------------------------------  

@dp.callback_query_handler(text="yangiliklar")    
async def statistikaUz(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>IT inkubatsiya markazida yangi Informatsion kurslar tashkil etilmoqda !</b> ", reply_markup=YangiliklarUz)

#--------------------------------------------Axborot texnologiyalari kafedrasi---------------------

@dp.callback_query_handler(text="axborotKafedra")    
async def axborotKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Kafedra mudiri: \n \n Suropov Baxodir Maydonovich \n Bog'lanish: +998973824888 </b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n 1)Suropov Baxodir Maydonovich- PhD. Dotsent \n 2) Panjiyev Samijon Aliqulovich – Katta о‘qituvchi \n 3)Boypolvonov Barot Djonqobulovich – Katta о‘qituvchi \n 4)Axmedova Barno Abdiyevna – Katta о‘qituvchi \n 5)Rajabov Jamshid Nasrillayevich – Katta о‘qituvchi \n 6)Jamalova Gulchexra Babakulovna – Assistent \n 7)Qahramonova Xumora Qahramonovna – Katta о‘qituvchi \n 8)Hamrayev Nodir Zokir о‘g‘li – Katta о‘qituvchi \n  9)Ergashev Nuriddin G‘ayratovich – Katta о‘qituvchi \n 10)Eshmurodov Azamat G‘uzorovich – Katta о‘qituvchi \n 11)Xoliqulov Bekzod Jovliyevich - Katta о‘qituvchi  \n 12)Shaynazarov Ravshan Mamayusubovich – Assistent \n 13)Ishqobilov Farrux Xayrilloyevich – Assistent \n 14)Tursunov Mirolim Ahmadovich – Assistent \n 15)Shukurov Akmal Uktamovich– Assistent \n 16)Zaripova Shaxlo Olimovna-Stajyor-o’qituvchi  \n 17)Xoliyorova Hilola Komil qizi- Stajyor- o’qituvchi", reply_markup=YangiliklarUz)

#--------------------------------------------Neft va Gaz ishi kafedrasi---------------------

@dp.callback_query_handler(text="neftGazKafedra")    
async def neftGazKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Neft va Gaz Kafedra mudiri: \n \n Sattorov Laziz Xolmurodovich \n Bog'lanish: +998752271054 </b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n fan doktorlari - 2 \n fan nomzodlari - 3 \n katta o‘qituvchilar - 12 \n assistentlar - 16 \n stajerlar - 3 \n\n", reply_markup=YangiliklarUz)

#--------------------------------------------TMJ kafedrasi----------------------------------

@dp.callback_query_handler(text="texnoJihozKafedra")    
async def texnoJihozKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Texnologik mashina va jihozlash kafedra mudiri: \n \n Sunnatov Zafar Ubaydullayevich \n Bog'lanish: +998 99 945 98 12 </b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n   professor - 1 \n dotsent, texnika fanlari nomzodi - 3 \n katta o‘qituvchi - 6 \n assistentlar - 8 \n \n ", reply_markup=YangiliklarUz)

#--------------------------------------------TJA kafedrasi---------------------

@dp.callback_query_handler(text="tjaavtomatikaKafedra")    
async def tjaavtomatikaKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Texnologik jarayonlar va avtomatlashtirish va boshqarish kafedra mudiri: \n \n Jurayev Aburayhon Xoliqulovich \n Bog'lanish: +998 90 607 34 84  </b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n iqtisod fanlari doktori - 1 \n  texnika fanlari nomzodi - 1 \n iqtisod fanlari nomzodi - 1 \n \n ", reply_markup=YangiliklarUz)

#--------------------------------------------Gidro inshootlar kafedrasi---------------------

@dp.callback_query_handler(text="gidroInshootKafedra")    
async def gidroInshootKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Gidravlika va gidro inshootlar kafedra mudiri: \n \n Eshev Sobir Samatovich \n Bog'lanish: +998972000577 </b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n professor - 3\n fan nomzodi, dotsentlar - 3 \n katta o‘qituvchi - 3 \n assistent - 7 \n stajyor - 1 ", reply_markup=YangiliklarUz)

#--------------------------------------------Transport vositalari muhandisligi kafedrasi---------------------

@dp.callback_query_handler(text="transportKafedra")    
async def transportKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>  Transport vositalari kafedra mudiri: \n \n Abduraxmonov O‘rol Nurmatovich \n Bog'lanish:   +998972290059</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)

#--------------------------------------------Umumtexnika fanlar kafedrasi---------------------

@dp.callback_query_handler(text="umumtexnikaKafedra")    
async def umumtexnikaKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Umumtexnika fanlar kafedra mudiri: \n \nIsmailov Ibrat Ilxomovich \n Bog'lanish:    +998939370033</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)

#-------------------------------------------- Foydali qazilmalar geologiyasi va razvetkasi kafedrasi---------------------

@dp.callback_query_handler(text="foydaliKonKafedra")    
async def foydaliKonKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>  Foydali qazilmalar geologiyasi va razvetkasi kafedra mudiri: \n \nTurdiyev Shahboz Shermamat o‘g‘li \n Bog'lanish:  +998912155151</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Konchilik ishi kafedrasi---------------------

@dp.callback_query_handler(text="konchilikKafedra")    
async def konchilikKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>  Konchilik ishi kafedrasi mudiri: \n \nShodiyev Abbos Ne’mat o‘g‘li \n Bog'lanish:  +998 90 722 66 88</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Ekologiya va mehnat muhofazasi kafedrasi---------------------

@dp.callback_query_handler(text="ekologiyaKafedra")    
async def ekologiyaKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>   Ekologiya va mehnat muhofazasi kafedrasi mudiri: \n \nEshonqulov Ravshan Abdurazaqovich \n Bog'lanish:  +99890 729 0370</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Kimyoviy texnologiyalar  kafedrasi---------------------

@dp.callback_query_handler(text="kimyoTexKafedra")    
async def kimyoTexKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>  Kimyoviy texnologiyalar  kafedrasi mudiri: \n \nRosilov Mansur Sirgiyevich \n Bog'lanish:   +998972220771</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Qishloq xo'jaligi mahsulotlarini saqlash kafedrasi---------------------

@dp.callback_query_handler(text="qishloqSaqlashKafedra")    
async def qishloqSaqlashKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Qishloq xo'jaligi mahsulotlarini saqlash kafedrasi mudiri: \n \nHakimova Muabara Xalilovna \n Bog'lanish:    +998998571727</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Issiqlik energetikasi kafedrasi---------------------

@dp.callback_query_handler(text="issiqlikKafedra")    
async def issiqlikKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Issiqlik energetikasi kafedrasi kafedrasi mudiri: \n \nFayziev To‘lqin Amirovich \n Bog'lanish:   +998912628488</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Elektr energetikasi kafedrasi---------------------

@dp.callback_query_handler(text="elektrKafedra")    
async def elektrKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Elektr energetikasi kafedrasi mudiri: \n \nFayziyev Maxmanazar Mansurovich \n Bog'lanish:  +99890 673-97-64</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Fizika va elektronika kafedrasi---------------------

@dp.callback_query_handler(text="fizikaElektrKafedra")    
async def fizikaElektrKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Fizika va elektronika kafedrasi mudiri: \n \nAliqulov Muysin Nortoshevich \n Bog'lanish:   +998 939356181</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Innovatsion iqtisodiyot kafedrasi---------------------

@dp.callback_query_handler(text="innoIqtisodKafedra")    
async def innoIqtisodKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Innovatsion iqtisodiyot kafedrasi mudiri: \n \nHamrayeva Sayyora Nasimovna \n Bog'lanish: +998904275580</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Buxgalteriya hisobi va audit kafedrasi---------------------

@dp.callback_query_handler(text="buxAuditKafedra")    
async def buxAuditKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Buxgalteriya hisobi va audit kafedrasi mudiri: \n \nAlikulov Azamat Tuygunovich\n Bog'lanish:  +998996696673</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Biznes va innovatsion menejment kafedrasi---------------------

@dp.callback_query_handler(text="biznesKafedra")    
async def biznesKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Biznes va innovatsion menejment kafedrasi mudiri: \n \nRaximov Anvar Norimovich\n Bog'lanish: +998914536377</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  O'zbekiston tarixi kafedrasi---------------------

@dp.callback_query_handler(text="uzTarixKafedra")    
async def uzTarixKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> O'zbekiston tarixi kafedrasi mudiri: \n \nErgasheva Yulduz Alimovna\n Bog'lanish: +998906170012</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------   Ijtimoiy fanlar kafedrasi---------------------

@dp.callback_query_handler(text="ijtimoiyKafedra")    
async def ijtimoiyKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Ijtimoiy fanlar kafedrasi mudiri: \n \nAxmedov Bekzod Abdiraxmonovich\n Bog'lanish: +998912177503</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------    O'zbek va rus tillari kafedrasi---------------------

@dp.callback_query_handler(text="uzbRusKafedra")    
async def uzbRusKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> O'zbek va rus tillari kafedrasi mudiri: \n \nBegimov Odil To‘xtamishovich\n Bog'lanish: +998939088835</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------     Xorijiy tillar kafedrasi---------------------

@dp.callback_query_handler(text="xorijiyKafedra")    
async def xorijiyKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Xorijiy tillar kafedrasi mudiri: \n \nXoliyorov Bunyod Husanovich\n Bog'lanish: +998945263885</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Jismoniy tarbiya kafedrasi---------------------

@dp.callback_query_handler(text="jismoniyKafedra")    
async def jismoniyKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Jismoniy tarbiya  kafedrasi mudiri: \n \nArislonov Ilhom Toshtemirovich\n Bog'lanish: +998907164020</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Muqobil energiya manbaalari kafedrasi---------------------

@dp.callback_query_handler(text="muqobilEnergiyaKafedra")    
async def muqobilEnergiyaKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Muqobil energiya manbaalari kafedrasi mudiri: \n \nDavlonov Xayrulla Allamurotovich\n Bog'lanish: +998904416980</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Qishloq xo'jaligini mexanizatsiyalash kafedrasi---------------------

@dp.callback_query_handler(text="qishloqKafedra")    
async def qishloqKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Qishloq xo'jaligini mexanizatsiyalash kafedrasi mudiri: \n \nBatirov Zafar Lutfullayevich\n Bog'lanish: +998914648622</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------Geodeziya, kadastr va yerdan foydalanish kafedrasi---------------------

@dp.callback_query_handler(text="geodeziyaKafedra")    
async def geodeziyaKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Geodeziya, kadastr va yerdan foydalanish kafedrasi mudiri: \n \nAliqulov G‘olib Nortoshevich\n Bog'lanish: +998936972019</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Neft va gazni qayta ishlash kafedrasi---------------------

@dp.callback_query_handler(text="neftgazKafedra")    
async def neftgazKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b> Neft va gazni qayta ishlash kafedrasi mudiri: \n \nDustqobilov Eldor Nurmamatovich\n Bog'lanish: +99893-902-12-32</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#--------------------------------------------  Oziq ovqat mahsulotlari kafedrasi---------------------

@dp.callback_query_handler(text="oziqOvqatKafedra")    
async def oziqOvqatKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>  Oziq ovqat mahsulotlari kafedrasi mudiri: \n \nBoqiyev Gulomjon Ochilovich\n Bog'lanish: +99897 222 55 27</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


#-------------------------------------------- Oliy matematika kafedrasi---------------------

@dp.callback_query_handler(text="oliyMatemKafedra")    
async def oliyMatemKafedra(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer(parse_mode="HTML",text="⚫️ <b>Oliy matematika kafedrasi mudiri: \n \nEshmatov Bahodir Eliyevich\n Bog'lanish: +998 91 643 40 53</b> \n  Qabul kunlari: Dushanba-Juma (14:00-17:00) \n Kafedrada faoliyat yuritayotgan professor-о‘qituvchilar  rо‘yxati : \n \n \n \n ", reply_markup=YangiliklarUz)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


