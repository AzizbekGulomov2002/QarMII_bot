from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="🇺🇿 o'zbekcha",callback_data="uz"),
            InlineKeyboardButton(text="🇷🇺 ruscha",callback_data="ru"),
        ]       
    ]
)

uzHeader = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎓 Bakalavr",callback_data="bakalavr"),
            InlineKeyboardButton(text="💼 Magistr",callback_data="magistr"),
           
        ],
        
        [
            
            InlineKeyboardButton(text="🏛 Universitet haqida",callback_data="haqida"),
            InlineKeyboardButton(text="⚙️ Tilni o'zgartirish",callback_data="til"),
            
        ],
        
        
        
       
    ]
)


ruHeader = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🎓 Бакалавр",callback_data="бакалавр"),
            InlineKeyboardButton(text="💼 Магистр",callback_data="магистр"),
           
        ],
        
        [
            InlineKeyboardButton(text="🏛 Об Университете",callback_data="об"),
            InlineKeyboardButton(text="⚙️ Изменить язык",callback_data="язык"),
            
        ],
        
        
       
    ]
)



bakalavrUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek fakultetlari",callback_data="uzfak"),     
        ],
        
        [      
            InlineKeyboardButton(text="🇷🇺 Rus fakultetlari",callback_data="rusfak"),       
        ],
        
        [      
            InlineKeyboardButton(text="🇧🇾 Belarus fakultetlari",callback_data="belfak"),   
        ],
        
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="<<UzFak"),
            InlineKeyboardButton(text="⚙️ Tilni o'zgartirish",callback_data="til"),
            
           
        ],
       
    ]
)


bakalavrRu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 Узбекские факультеты",callback_data="uzfak"),
            InlineKeyboardButton(text="🇷🇺 Русские факультеты",callback_data="rusfak"),
            InlineKeyboardButton(text="🇧🇾 Белорусские факультеты",callback_data="belfak"),
           
        ],
        
        [
            InlineKeyboardButton(text="<< Назад",callback_data="<<RuFak"),
            InlineKeyboardButton(text="⚙️ Изменить язык",callback_data="til"),
            
           
        ],
       
    ]
)
# ----------------------Fakultetlar ro'yxati Uzb tilida------------------------------------

UzFakultetUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Iqtisodiyot",callback_data="iqtisod"),                     
        ],  
        
        [       
            InlineKeyboardButton(text="Neft va Gaz",callback_data="neftgaz"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Energetika",callback_data="energetika"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Sanoat texnologiyalari",callback_data="sanoat"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="Kasb hunar ta'limi",callback_data="kasbHunar"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="Muhandislik",callback_data="muhandislik"),                        
        ],
        
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="bakalavr"),
            InlineKeyboardButton(text="⚙️ Tilni o'zgartirish",callback_data="til"),
            
           
        ],     
    ]
)

# ----------------------Fakultetlar ro'yxati Rus tilida------------------------------------

RuFakultetRu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Экономика",callback_data="iqtisod"),                     
        ],  
        
        [       
            InlineKeyboardButton(text="Нефтъ и Газ",callback_data="neftgaz"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Энергетика",callback_data="energetika"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Промышленные технологии",callback_data="sanoat"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="Профессионально-техническое образование",callback_data="kasbHunar"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="Инжиниринг",callback_data="muhandislik"),                        
        ],
        
        [
            InlineKeyboardButton(text="<< Назад",callback_data="<<iqtisod"),
            InlineKeyboardButton(text="⚙️ Изменить язык",callback_data="til"),
            
           
        ],     
    ]
)


UzIqtisodUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bank ishi va auditi",callback_data="bank"),                     
        ],  
        
        [       
            InlineKeyboardButton(text="Buxgalteriya hisobi va audit",callback_data="bugalter"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Iqtisodiyot",callback_data="iqtisod"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Logistika",callback_data="logistika"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="Moliya va moliyaviy texnologiyalar",callback_data="moliya"),                       
        ], 
        
        
        
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
            InlineKeyboardButton(text="⚙️ Tilni o'zgartirish",callback_data="til"),
            
           
        ],     
    ]
)



