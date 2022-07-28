
import sqlite3


class Sql:
    def __init__(self):
        self.connection = sqlite3.connect("Univer.db", check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def createDb(self, data):
        self.cursor.execute(f""" CREATE table IF NOT EXISTS {data[0][0]} (
            id integer primary key, 
            telegram_id integer,
            ism varchar(50),
            yosh integer, 
            tel_raqam varchar(13),
            murojaat text
            )""")
        self.cursor.execute(f""" INSERT INTO {data[0][0]} (
            telegram_id, ism, yosh, tel_raqam, murojaat
            )
            values(?,?,?,?,?)    
            """, data[1]
            )
        return self.connection.commit()
        
    def updateDB(self,data):
        self.cursor.execute(f""" UPDATE {data[0]} SET ism = "{data[1]}" WHERE telegram_id = {data[2]}""")
        return self.connection.commit()
    
    def deleteDb(self, data):
        self.cursor.execute(f""" DELETE FROM {data[0]} WHERE telegram_id = {data[1]}""")
        return self.connection.commit()
    
data = [
    [
        "Aziz"
        
    ],
    [
        9898985521, "Azizbek", 20, "+998996671529", "Salom"
    ]
    
]

db = Sql()
# db.createDb(data)
# dataUpdate = ["Aziz", "Azizbek ", 9898985521]
# db.updateDB(dataUpdate)
dataDelete = ["Aziz", 9898985521 ]
db.deleteDb(dataDelete)