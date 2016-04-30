import sqlite3
import datetime



conn = sqlite3.connect('TranDB.db')
c = conn.cursor()


#-----RETRIEVE INFO-----#

def getCell(cell):
    c.execute("SELECT * FROM LastCheck WHERE ID =?", str(cell))
    return c.fetchall()

inCell = getCell(2)

print inCell


#conn.commit()

#-----ADD INFO-----#

def insertCell(add):
    c.execute("INSERT INTO LastCheck (DateTime) VALUES (?)", (add,))

insertCell('Test Four')

#conn.commit()
