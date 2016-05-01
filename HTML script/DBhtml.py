import sqlite3

conn = sqlite3.connect('Content Database.db')
c = conn.cursor()

#-----RETRIEVE RECORD-----#

def getName():
    c.execute("SELECT Name FROM Content WHERE ID =1")
    return c.fetchall()


def getContent():
    c.execute("SELECT HTML FROM Content WHERE ID =5")
    return c.fetchall()

print(getName())
print(getContent())
