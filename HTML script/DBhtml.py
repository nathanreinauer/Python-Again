import sqlite3

conn = sqlite3.connect('Content Database.db')
c = conn.cursor()

nameID = 2
contentID = 3

#-----RETRIEVE RECORD-----#

def getName():
    c.execute("SELECT Name FROM Content WHERE ID ={}".format(str(nameID)))
    return c.fetchall()


def getContent():
    c.execute("SELECT HTML FROM Content WHERE ID ={}".format(str(contentID)))
    return c.fetchall()

print(getName())
print(getContent())
