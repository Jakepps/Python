#15
import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('C:/Users/Артём/source/repos/Jakepps/Python/LR16/SQL_Hotel.db')
        return con
        print("Соединение работает")
    except Error:
        print(Error)


def sql_hotel(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE hotel("
        "HotelID integer PRIMARY KEY,"
        "HotelName text,"
        "Stars integer)")

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(1, 'У Рубена',  5 )"
    )
    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(2, 'У Гиренки',  3 )"
    )

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(3, 'СерегаХостел00014', 0)"
    )

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(4, 'Кубгу', 100000)"
    )

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(5, 'фантазия кончилась', 10)"
    )

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(6, 'чичи', 5)"
    )
    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(7, 'мичи', 3)"
    )

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(8, 'ачи', 0)"
    )

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(9, 'апчхи', 100000)"
    )

    cursorObj.execute(
        "INSERT INTO hotel "
        "VALUES(10, 'будь здоров', 10)"
    )
    con.commit()

def sql_employee(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE employee("
        "WorkerID integer PRIMARY KEY,"
        "Name text,"
        "Number integer,"
        "Salary integer,"
        "Age integer)")

    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(1, 'Рубен', 891842432,2000,18)"
    )  
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(2, 'Авдотий', 8918424322,3333,10)"
    )
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(3, 'Даниил', 89184242332,10000,100)"
    )  
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(4, 'Кондруцкий', 89184242332,1,32)"
    )  

    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(5, 'Джонатан', 89184239432,2000,18)"
    )  
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(6, 'Джозеф', 892218424322,22222,78)"
    )
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(7, 'Джотаро',189184242332,222222,34)"
    )  
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(8, 'Джоске', 8918424233552,13,19)"
    )  
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(9, 'Джорно', 8913842432333,200000,25)"
    )   
        
    cursorObj.execute(
        "INSERT INTO employee "
        "VALUES(10, 'Джолин', 823913842432,2222,19)"
    )    

def sql_rooms(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE room("
        "roomID integer PRIMARY KEY,"
        "Number integer,"
        "Level integer,"
        "Floor integer)")

    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(1, 12,10,10)"
    )
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(2, 13,2,1)"
    )   
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(3, 1,1,1)"
    )   
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(4, 312,3,10)"
    )   
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(5, 33,9,123)"
    ) 
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(6, 1554,1320,110)"
    )
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(7, 32,76,17)"
    )   
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(8, 7,7,7)"
    )   
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(9, 777,888,19)"
    )   
    cursorObj.execute(
        "INSERT INTO room "
        "VALUES(10, 32,3131,3333)"
    )    

def sql_rating(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE rating("
        "HotelIDinRat integer PRIMARY KEY,"
        "Rat integer,"
        "TextRat text)"
    )

    cursorObj.execute(
        "INSERT INTO rating "
        "VALUES(1,5,'норм')"
    ) 
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(2, 10,'лучший')"
    ) 
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(3, 12334,'норм')"
    ) 
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(4,1,'база')"
    ) 
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(5, 10,'лучшие')"
    )  
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(6, 6,'вкусное пюре')"
    ) 
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(7, 2,'не вкусное пюре')"
    ) 
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(8, 1,'не нашел отель')"
    ) 
    cursorObj.execute(
        "INSERT INTO  rating "
        "VALUES(9, 19,'у вас работают татары?')"
    ) 
    cursorObj.execute(
        "INSERT INTO rating "
        "VALUES(10, 123,'яре яре дазе')"
    ) 

def sql_guest(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE guest("
        "GuestID integer PRIMARY KEY,"
        "Numb integer,"
        "NumRoom integer,"
        "Gender text)")
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(1, 12323213223,1,'муж')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(2, 892183964523,2,'жен')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(3, 89186363444,3,'муж')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(4, 8912386363444,4,'муж')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(5, 89123186363444,5,'жен')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(6, 122323213223,6,'муж')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(7, 83392183964523,7,'жен')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(8, 8918636344124,8,'муж')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(9, 891238636343244,9,'муж')"
    ) 
    cursorObj.execute(
        "INSERT INTO guest "
        "VALUES(10, 891231863634144,10,'жен')"
    ) 


def sql_update(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE hotel SET HotelName = "LOL" where HotelID = 1')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE hotel SET HotelName = "XD" where HotelID = 2')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employee SET Salary = 69000 where Age > 20')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE employee SET Age = 17 where Age = 18')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE room SET Level = 10 where Floor = 10')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE room SET Floor = 2 where Level > 12')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE rating SET Rat = 10 where TextRat = "норм"')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE rating SET HotelIDinRat = 2 where TextRat="взломал и изминил текст хд"')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE guest SET NumRoom = 16 where Gender = "муж"')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE guest SET NumRoom = 17 where Gender = "жен"')
    con.commit()

def sql_delete(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE from hotel where Stars = 1')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('DELETE from hotel where Stars < 1')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('DELETE from guest where Numb = 12323213223')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('DELETE from employee where Number = 891842432')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('DELETE from employee where WorkerID = 4')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('DELETE from rating where TextRat = "база"')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('DELETE from room where Number > 10')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('DELETE from guest where Numb = 89123186363444')
    con.commit()

def select(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:
        tablesList.append(tab[0])

    for listItem in tablesList:
        print(f"Вывод содержимого таблицы {listItem}")
        cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]

con=sql_connection()

sql_hotel(con)
sql_employee(con)
sql_rooms(con)
sql_rating(con)
sql_guest(con)


select(con)
print("ВЫВОД АПДЕЙТА")
sql_update(con)
select(con)
print("ВЫВОД УДАЛЕНИЯ")
sql_delete(con)
select(con)