from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="πΊπΏ o'zbekcha",callback_data="uz"),
            InlineKeyboardButton(text="π·πΊ ruscha",callback_data="ru"),
        ]       
    ]
)

uzHeader = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="π Bakalavr",callback_data="bakalavr"),
            InlineKeyboardButton(text="πΌ Magistr",callback_data="magistrUz"),
           
        ],
        
        [
            
            InlineKeyboardButton(text="π Institut haqida",callback_data="haqida"),
            InlineKeyboardButton(text="π Yangiliklar",callback_data="yangiliklar"),
            
        ],

        [
            InlineKeyboardButton(text="π Statistika",callback_data="statistikaUz"),
            InlineKeyboardButton(text="πͺ Rektorat",callback_data="rektoratUz"),
            
        ],
        
        
        
       
    ]
)
#-------------------------------YANGILIKLAR IT KURSLAR -------------------------------------
YangiliklarUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="kafedraUz"),
        ]
        
    ]
)
#-------------------------------STATISTIKA -------------------------------------
StatistikaUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="<<UzFak"),
        ]
        
    ]
)
#-------------------------------UNIVERSITET HAQIDA-------------------------------------
UniverHaqidaUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="<<UzFak"),
        ]
        
    ]
)

#-------------------------------REKTORAT BO'LIMI-------------------------------------
RektoratUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text="Rektoratga murojaat", callback_data="rektorQabulUz")
           
        ],
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="<<UzFak"),
        ]
        
    ]
)

#-------------------------------MAGISTRATURA-------------------------------------
MagistrUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="<<UzFak"),
        ]
        
    ]
)


ruHeader = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="π ΠΠ°ΠΊΠ°Π»Π°Π²Ρ",callback_data="Π±Π°ΠΊΠ°Π»Π°Π²Ρ"),
            InlineKeyboardButton(text="πΌ ΠΠ°Π³ΠΈΡΡΡ",callback_data="ΠΌΠ°Π³ΠΈΡΡΡ"),
           
        ],
        
        [
            InlineKeyboardButton(text="π ΠΠ± Π£Π½ΠΈΠ²Π΅ΡΡΠΈΡΠ΅ΡΠ΅",callback_data="ΠΎΠ±"),
            InlineKeyboardButton(text="βοΈ ΠΠ·ΠΌΠ΅Π½ΠΈΡΡ ΡΠ·ΡΠΊ",callback_data="ΡΠ·ΡΠΊ"),
            
        ],
        
        
       
    ]
)



bakalavrUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πΊπΏ O'zbek fakultetlari",callback_data="uzfak"),
            InlineKeyboardButton(text="π·πΊ Rus fakultetlari",callback_data="rusfak"),     
        ],     
        [      
            InlineKeyboardButton(text="π§πΎ Belarus fakultetlari",callback_data="belfak"), 
            InlineKeyboardButton(text="βͺοΈ Kafedralar",callback_data="kafedraUz"),  
        ],
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="<<UzFak"),
        ],
       
    ]
)


#-------------------------------KAFEDRALAR RO'YXATI-------------------------------------
KafedraUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1) Axborot texnologiyalari",callback_data="axborotKafedra"),
            InlineKeyboardButton(text="2) Neft va Gaz ishi",callback_data="neftGazKafedra"),
        ],
        [
            InlineKeyboardButton(text="3)Texnologik mashina va jihozlash",callback_data="texnoJihozKafedra"),
            InlineKeyboardButton(text="4) Gidravlika va gidro inshootlar",callback_data="gidroInshootKafedra"),
        ],
        [
            InlineKeyboardButton(text="5) Transport vositalari",callback_data="transportKafedra"),
            InlineKeyboardButton(text="6) Umumtexnika fanlar",callback_data="umumtexnikaKafedra"),
        ],
        [
            InlineKeyboardButton(text="7) Foydali qazilmalar geologiyasi va razvetkasi",callback_data="foydaliKonKafedra"),
            InlineKeyboardButton(text="8) Konchilik ishi",callback_data="konchilikKafedra"),
        ],

        [
            InlineKeyboardButton(text="9) Ekologiya va mehnat muhofazasi",callback_data="ekologiyaKafedra"),
            InlineKeyboardButton(text="10) Kimyoviy texnologiyalar",callback_data="kimyoTexKafedra"),
        ],
        [
            InlineKeyboardButton(text="11) Qishloq xo'jaligi mahsulotlarini saqlash",callback_data="qishloqSaqlashKafedra"),
            InlineKeyboardButton(text="12) Issiqlik energetikasi",callback_data="issiqlikKafedra"),
        ],

        [
            InlineKeyboardButton(text="13) Elektr energetikasi",callback_data="issiqlikKafedra"),
            InlineKeyboardButton(text="14) Fizika va elektronika",callback_data="fizikaElektrKafedra"),
        ],
        [
            InlineKeyboardButton(text="15) Innovatsion iqtisodiyot",callback_data="innoIqtisodKafedra"),
            InlineKeyboardButton(text="16) Buxgalteriya hisobi va audit",callback_data="buxAuditKafedra"),
        ],

        [
            InlineKeyboardButton(text="17) Biznes va innovatsion menejment",callback_data="biznesKafedra"),
            InlineKeyboardButton(text="18) O'zbekiston tarixi",callback_data="uzTarixKafedra"),
        ],
        [
            InlineKeyboardButton(text="19) Ijtimoiy fanlar",callback_data="ijtimoiyKafedra"),
            InlineKeyboardButton(text="20) O'zbek va rus tillari",callback_data="uzbRusKafedra"),
        ],
        [
            InlineKeyboardButton(text="21) Xorijiy tillar ",callback_data="xorijiyKafedra"),
            InlineKeyboardButton(text="22) Jismoniy tillar ",callback_data="jismoniyKafedra"),
        ],

        [
            InlineKeyboardButton(text="23) Muqobil energiya manbaalari ",callback_data="muqobilEnergiyaKafedra"),
            InlineKeyboardButton(text="24) Qishloq xo'jaligini mexanizatsiyalash",callback_data="qishloqKafedra"),
        ],
        [
            InlineKeyboardButton(text="25) Geodeziya, kadastr va yerdan foydalanish",callback_data="geodeziyaKafedra"),
            InlineKeyboardButton(text="26) Neft va gazni qayta ishlash",callback_data="neftGazKafedra"),
        ],
        [
            InlineKeyboardButton(text="27) Moliya",callback_data="moliyaKafedra"),
            InlineKeyboardButton(text="28) Oziq ovqat mahsulotlari",callback_data="oziqOvqatKafedra"),
        ],

        [
            InlineKeyboardButton(text="29) Oliy matematika",callback_data="oliyMatemKafedra"),
            InlineKeyboardButton(text="<< Ortga",callback_data="bakalavr"),
        ],


        
    ]
)

#--------------------------------Kafedra 1-------------------------------
AxborotoKafedra = InlineKeyboardMarkup(
    inline_keyboard=[        
        

        [
            InlineKeyboardButton(text="<< Ortga",callback_data="kafedraUz"),
        ],     
    ]
)


bakalavrRu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πΊπΏ Π£Π·Π±Π΅ΠΊΡΠΊΠΈΠ΅ ΡΠ°ΠΊΡΠ»ΡΡΠ΅ΡΡ",callback_data="uzfak"),
            InlineKeyboardButton(text="π·πΊ Π ΡΡΡΠΊΠΈΠ΅ ΡΠ°ΠΊΡΠ»ΡΡΠ΅ΡΡ",callback_data="rusfak"),
            InlineKeyboardButton(text="π§πΎ ΠΠ΅Π»ΠΎΡΡΡΡΠΊΠΈΠ΅ ΡΠ°ΠΊΡΠ»ΡΡΠ΅ΡΡ",callback_data="belfak"),
           
        ],
        
        [
            InlineKeyboardButton(text="<< ΠΠ°Π·Π°Π΄",callback_data="<<RuFak"),
            InlineKeyboardButton(text="βοΈ ΠΠ·ΠΌΠ΅Π½ΠΈΡΡ ΡΠ·ΡΠΊ",callback_data="til"),
            
           
        ],
       
    ]
)
# ----------------------Fakultetlar ro'yxati Uzb tilida------------------------------------

UzFakultetUz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1) Iqtisodiyot",callback_data="iqtisod"),
            InlineKeyboardButton(text="2) Neft va Gaz",callback_data="neft"),                      
        ],  
        
       
        
        [       
            InlineKeyboardButton(text="3) Energetika",callback_data="energetika"), 
            InlineKeyboardButton(text="4) Sanoat texnologiyalari",callback_data="sanoat"),                        
        ],      
        [       
            InlineKeyboardButton(text="5) Geologiya va konchilik",callback_data="geologiya"),   
            InlineKeyboardButton(text="6) Muhandislik texnikasi",callback_data="muhandislik"),                    
        ], 

        [       
            InlineKeyboardButton(text="7) Elektronika va avtomatika",callback_data="elektroAvto"),  
            InlineKeyboardButton(text="π° Kontrakt va Stipendiya",callback_data="kontrakUz"),                        
        ],      
        [
            InlineKeyboardButton(text="<< Ortga",callback_data="bakalavr"),         
           
        ],     
    ]
)

#--------------------------------KATRAKT BUJJET-------------------------------
KantrakBujetUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        

        [
            InlineKeyboardButton(text="<< Ortga",callback_data="bakalavr"),
        ],     
    ]
)

# ----------------------Fakultetlar ro'yxati Rus tilida------------------------------------

RuFakultetRu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Π­ΠΊΠΎΠ½ΠΎΠΌΠΈΠΊΠ°",callback_data="iqtisod"),                     
        ],  
        
        [       
            InlineKeyboardButton(text="ΠΠ΅ΡΡΡ ΠΈ ΠΠ°Π·",callback_data="NeftGaz"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="Π­Π½Π΅ΡΠ³Π΅ΡΠΈΠΊΠ°",callback_data="energetika"),                        
        ], 
        
        [       
            InlineKeyboardButton(text="ΠΡΠΎΠΌΡΡΠ»Π΅Π½Π½ΡΠ΅ ΡΠ΅ΡΠ½ΠΎΠ»ΠΎΠ³ΠΈΠΈ",callback_data="sanoat"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="ΠΠ΅ΠΎΠ»ΠΎΠ³ΠΈΡ ",callback_data="kasbHunar"),                       
        ], 
        
        [       
            InlineKeyboardButton(text="ΠΠ½ΠΆΠΈΠ½ΠΈΡΠΈΠ½Π³",callback_data="muhandislik"),                        
        ],

        [       
            InlineKeyboardButton(text="Elektronika va avtomatika",callback_data="elektoAvto"),                        
        ],
        
        [
            InlineKeyboardButton(text="<< ΠΠ°Π·Π°Π΄",callback_data="<<iqtisod"),
            InlineKeyboardButton(text="βοΈ ΠΠ·ΠΌΠ΅Π½ΠΈΡΡ ΡΠ·ΡΠΊ",callback_data="til"),
            
           
        ],     
    ]
)

#--------------------------------IQTISODIYOT FAKULTETI YO'NALISHLARI BO'LIMI (BANK, BUGALTERIYA)-------------------------------
UzIqtisodUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="π’Dekanat",callback_data="DekanUzIqtisod"),  
            
            
        ],

         [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
        ],     
    ]
)

#--------------------------------IQTISODIYOT FAKULTETI DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
IqtisodDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πDekanatga murojaat",callback_data="UzIqtisodDekanat"),     
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
            InlineKeyboardButton(text="π’Dekanat",callback_data="DekanNeftUz"),   
            
         
        ],

         [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
        ],     
    ]
)

#--------------------------------Neft Gaz FAKULTETI DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzNeftGazDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πDekanatga murojaat",callback_data="UzNeftGazDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="neft"),     
        ],  
    ]
)


#--------------------------------Energetika FAKULTETI YO'NALISHLARI BO'LIMI (Konchilik, gaz quduq...)-------------------------------
EnergiyaUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="π’Dekanat",callback_data="DekanEnergiyaUz"),   
            
            
        ],

         [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
        ],     
    ]
)


#--------------------------------Energetika FAKULTETI DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzEnergiyaDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πDekanatga murojaat",callback_data="UzEnergiyaDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="energetika"),     
        ],  
    ]
)


#--------------------------------Sanoat FAKULTETI YO'NALISHLARI BO'LIMI -------------------------------
SanoatUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="π’Dekanat",callback_data="DekanSanoatUz"),   
            
           
        ],

         [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
        ],     
    ]
)


#--------------------------------Energetika FAKULTETI DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzSanoatDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πDekanatga murojaat",callback_data="UzSanoatDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="sanoat"),     
        ],  
    ]
)


#--------------------------------Geologiya va konchilik FAKULTETI YO'NALISHLARI BO'LIMI-------------------------------
GeologiyaUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="π’Dekanat",callback_data="DekanGeologiyaUz"),   
            
            
        ],

         [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
        ],     
    ]
)


#--------------------------------Geologiya FAKULTETI DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzGeologiyaDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πDekanatga murojaat",callback_data="UzGeologiyaDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="sanoat"),     
        ],  
    ]
)

#--------------------------------Muhandislik FAKULTETI YO'NALISHLARI BO'LIMI-------------------------------
Muhandislikuz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="π’Dekanat",callback_data="DekanMuhandislikUz"),   
            
            
        ],

         [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
        ],     
    ]
)

#--------------------------------Muhandislik DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzMuhandisDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πDekanatga murojaat",callback_data="UzMuhandisDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="muhandis"),     
        ],  
    ]
)

#--------------------------------Elektronika va Avtomatika FAKULTETI YO'NALISHLARI BO'LIMI-------------------------------
ElektroAvtoUz = InlineKeyboardMarkup(
    inline_keyboard=[        
        [
            InlineKeyboardButton(text="π’Dekanat",callback_data="ElektroavtoDekanat"),   
            
           
        ],

         [
            InlineKeyboardButton(text="<< Ortga",callback_data="uzfak"),
        ],     
    ]
)

#--------------------------------Elektronika DEKANATI BO'LIMI (DEKANGA MUROJAAT)-------------------------------
UzElektroAvtoDekanat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="πDekanatga murojaat",callback_data="UzElektroavtoDekanat"),     
        ],   
        [
            InlineKeyboardButton(text="<< Ortga ",callback_data="elektroAvto"),     
        ],  
    ]
)