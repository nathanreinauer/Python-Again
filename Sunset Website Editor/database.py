import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()

conn = sqlite3.connect('movielist.db')
c = conn.cursor()

def getContent():
    c.execute(("SELECT * FROM Movies WHERE ID ='{}'").format(contentBox.get()[0:2]))
    return c.fetchall()

def buttClick():
    print (getContent())

def forComboBox():
    c.execute("SELECT ID, Format, Title FROM Movies ORDER BY ID DESC LIMIT 0,6")
    return c.fetchall()


contentBox = StringVar()
combobox = ttk.Combobox(root, textvariable = contentBox, state='readonly')
combobox.grid(row=0,column=0)
combobox.config(values = forComboBox())

contentBox.set('Select movie:')

ttk.Button(text='Print Record',command=buttClick).grid(row=1,column=0,padx=5,pady=5,sticky='w')




##print(getContent())
print(forComboBox())

root.mainloop()

