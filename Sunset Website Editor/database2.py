import sqlite3
from tkinter import *
from tkinter import ttk
import time
from datetime import date

root = Tk()

conn = sqlite3.connect('movielist.db')
c = conn.cursor()


varID = '20'

def getSynopsis():
    c.execute(("SELECT Synopsis FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()

def getTitle():
    c.execute(("SELECT Title FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()

def getCast():
    c.execute(("SELECT Actors FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()

def getRating():
    c.execute(("SELECT Rating FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()

def getDates():
    c.execute(("SELECT Dates FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()

def getRuntime():
    c.execute(("SELECT Runtime FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()

def getTrailer():
    c.execute(("SELECT Trailer FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()

def getImage():
    c.execute(("SELECT Image FROM Movies WHERE ID ='{}'").format(varID))#.format(contentBox.get()[0:2]))
    return c.fetchall()


def buttClick():
    synopsis = str(getTitle())[3:-4]
    text_summary.insert(1.0, synopsis)

    dates = str(getDates())[3:-4]
    text_title.insert(1.0, dates)

    datesTemp = str(getDates()).split(',', 1)[0]
    datesEpoch = datesTemp[3:]+', ' + str(date.today().year)
    date_time = datesEpoch
    pattern = '%B %d, %Y'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    print (epoch)

    




ttk.Label(text='Synopsis',foreground='#ccffff').grid(row=6,column=0,pady=5, sticky='e')
text_summary=Text(width=75,height=9, wrap=WORD)
text_summary.grid(row=6,column=1,columnspan=3,padx=5, sticky='w')

ttk.Label(text='Title',foreground='#ccffff').grid(row=6,column=0,pady=5, sticky='e')
text_title=Text(width=75,height=1, wrap=WORD)
text_title.grid(row=1,column=1,columnspan=3,padx=5, sticky='w')



ttk.Button(text='Print Record',command=buttClick).grid(row=1,column=0,padx=5,pady=5,sticky='w')







root.mainloop()

