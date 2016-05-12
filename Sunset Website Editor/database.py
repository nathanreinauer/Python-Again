import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()

conn = sqlite3.connect('movielist.db')
c = conn.cursor()

contentBox = StringVar()
combobox = ttk.Combobox(root, textvariable = contentBox, state='readonly')
combobox.pack()
combobox.config(values = ('1', '2', '3', '4', '5'))

contentBox.set('Select content:')

def getContent():
    c.execute("SELECT * FROM Movies WHERE ID ='{}'".format(contentBox.get()))
    return c.fetchall()

print(getContent())

root.mainloop()

