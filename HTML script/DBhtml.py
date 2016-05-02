import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()

conn = sqlite3.connect('Content Database.db')
c = conn.cursor()

contentBox = StringVar()
combobox = ttk.Combobox(root, textvariable = contentBox, state='readonly')
combobox.pack()
combobox.config(values = ('Clothes', 'Food', 'Movies', 'Toys', 'Sand'))

contentBox.set('Select content:')

def getContent():
    c.execute("SELECT HTML FROM Content WHERE conName ='{}'".format(contentBox.get()))
    return c.fetchall()

##print(getContent())

root.mainloop()

