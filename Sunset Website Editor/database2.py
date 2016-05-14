import sqlite3
from tkinter import *
from tkinter import ttk
import time
from datetime import date

root = Tk()

conn = sqlite3.connect('movielist.db')
c = conn.cursor()


varID = '20'
varID2 = '21'

        # Grabs info from database on 'Select' button click
def getContent():
    c.execute("SELECT ID, Format, Title FROM Movies WHERE ID ='{}'".format(contentBox.get()))
    fetch = (c.fetchall())
    return str(fetch)#[3:-4]

        # Puts values in combobox
def getValues(x):
    c.execute("SELECT ID, Format, Title FROM Movies WHERE ID ='{}'".format(x))#(contentBox.get()))
    fetch = (c.fetchall())
    return str(fetch)[1:-1]



def addRecord():
    newTitle = text_title.get(1.0, 'end')
    newSynopsis = text_summary.get(1.0, 'end')
    c.execute("INSERT INTO Movies (Title, Synopsis) VALUES ('{}','{}');".format(newTitle, newSynopsis))
    conn.commit()
    print (newTitle + newSynopsis)





def test():
    print (getContent())

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
    synopsis = str(getTitle())[3:-4] # Insert field into textbox
    text_summary.insert(1.0, synopsis)

    dates = str(getDates())[3:-4] # Insert field into textbox
    text_title.insert(1.0, dates)

    datesTemp = str(getDates()).split(',', 1)[0] # Grab the first day from date field
    datesEpoch = datesTemp[3:]+', ' + str(date.today().year) # Slice the ends off and add current year
    date_time = datesEpoch # Not sure what this is for
    pattern = '%B %d, %Y' # Tell python what the date format is
    epoch = int(time.mktime(time.strptime(date_time, pattern))) # Convert it to Epoch
    print (epoch)

    




ttk.Label(text='Synopsis',foreground='#ccffff').grid(row=6,column=0,pady=5, sticky='e')
text_summary=Text(width=75,height=9, wrap=WORD)
text_summary.grid(row=6,column=1,columnspan=3,padx=5, sticky='w')

ttk.Label(text='Title',foreground='#ccffff').grid(row=6,column=0,pady=5, sticky='e')
text_title=Text(width=75,height=1, wrap=WORD)
text_title.grid(row=1,column=1,columnspan=3,padx=5, sticky='w')



def getRecord():
    c.execute(("SELECT * FROM Movies WHERE ID ='{}'").format(contentBox.get()[0:2]))
    return c.fetchall()

def buttPrint():
##    print (getRecord())
    addRecord()

def forComboBox():
    c.execute("SELECT ID, Format, Title FROM Movies ORDER BY ID DESC LIMIT 0,10")
    return c.fetchall()


contentBox = StringVar()		 
combobox = ttk.Combobox(root, textvariable = contentBox, state='readonly', width=30)		  	 
combobox.grid(row=0,column=0)
combobox.config(values = forComboBox())
contentBox.set('Select movie:')

ttk.Button(text='Print Record',command=buttPrint).grid(row=1,column=0,padx=5,pady=5,sticky='w')


print(getValues(varID))
print(getValues(varID2))

root.mainloop()

