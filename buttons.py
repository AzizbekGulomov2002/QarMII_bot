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

        [
            InlineKeyboardButton(text="📈 Statistika",callback_data="statistikaUz"),
            InlineKeyboardButton(text="🏪 Rektorat",callback_data="rektoratUz"),
            
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
            InlineKeyboardButton(text="Iqtisodiyot Fakulteti",callback_data="iqtisod"),                     
        ],  
        
        [       
            InlineKeyboardButton(text="Neft va Gaz Fakulteti",callback_data="neft"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Energetika Fakulteti",callback_data="energetika"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Sanoat texnologiyalari Fakulteti",callback_data="sanoat"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="Kasb hunar ta'limi Fakulteti",callback_data="kasbHunar"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="Muhandislik Fakulteti",callback_data="muhandislik"),                        
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
            InlineKeyboardButton(text="Нефтъ и Газ",callback_data="NeftGaz"),                        
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

#--------------------------------IQTISODIYOT FAKULTETI YO'NALISHLARI BO'LIMI (BANK, BUGALTERIYA)-------------------------------
UzIqtisodUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
            InlineKeyboardButton(text="⚙️ Tilni o'zgartirish",callback_data="til"),     
        ],

         [
            InlineKeyboardButton(text="🏢Dekanat",callback_data="DekanUzUqtisod"),     
        ],     
    ]
)

#--------------------------------IQTISODIYOT FAKULTETI DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzIqtisodDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝Dekanatga murojaat",callback_data="UzIqtisodDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="iqtisod"),     
        ],  
    ]
)
#--------------------------------Neft Gaz FAKULTETI YO'NALISHLARI BO'LIMI (Konchilik, gaz quduq...)-------------------------------
NeftGazUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
            InlineKeyboardButton(text="⚙️ Tilni o'zgartirish",callback_data="til"),     
        ],

         [
            InlineKeyboardButton(text="🏢Dekanat",callback_data="DekanNeftUz"),     
        ],     
    ]
)

#--------------------------------Neft Gaz FAKULTETI DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzNeftGazDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝Dekanatga murojaat",callback_data="UzNeftGazDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="neft"),     
        ],  
    ]
)

