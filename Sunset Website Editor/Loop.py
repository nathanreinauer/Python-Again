import webbrowser
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from datetime import date
import datetime
import os
import csv

conn = sqlite3.connect('movielist.db')
c = conn.cursor()


y =0

    
def fetch(year): 
    c.execute('SELECT Dates, Title, Format FROM Movies WHERE Dates LIKE "%{}%";'.format(year))
    return c.fetchall()

print (fetch(3))


def addToPastPage():
    year2016 = fetch(2016)
    year2017 = fetch(2017)
    year2018 = fetch(2018)
    year2019 = fetch(2019)
    year2020 = fetch(2020)
    year2021= fetch(2021)
