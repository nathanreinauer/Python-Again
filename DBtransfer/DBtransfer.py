import sqlite3
from datetime import *



conn = sqlite3.connect('TranDB.db')
c = conn.cursor()
today = datetime.now()
timeNow = today.strftime("%a, %b %d %Y at %I:%M %p")

#-----ADD INFO-----#

def insertCell(add):
    c.execute("INSERT INTO LastCheck (DateTime) VALUES (?)", (add,))
    conn.commit()
    
insertCell(timeNow)




#-----RETRIEVE LATEST RECORD-----#

def getCell():
    c.execute("SELECT * FROM LastCheck ORDER BY ID DESC LIMIT 1")
    return c.fetchall()

dateTimeCell = str(getCell())[8:-3]
print dateTimeCell

