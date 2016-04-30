import sqlite3
import datetime



conn = sqlite3.connect('TranDB.db')
c = conn.cursor()


#-----RETRIEVE LATEST RECORD-----#

def getCell():
    c.execute("SELECT * FROM LastCheck ORDER BY ID DESC LIMIT 1")
    return c.fetchall()

print getCell()

#-----ADD INFO-----#

def insertCell(add):
    c.execute("INSERT INTO LastCheck (DateTime) VALUES (?)", (add,))

insertCell('Test Five')

#conn.commit()
