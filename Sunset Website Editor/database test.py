
import sqlite3


conn = sqlite3.connect('movielist.db')
c = conn.cursor()

movieVar1 = "The Jungle Book"
movieVar2 = "Captain America"
movieVar3 = "Shit"
movieVar4 = "Big Wedding"
movieVar5 = "The Jungle Book"

def findDupes():
    if movieVar1 in (movieVar2, movieVar3, movieVar4, movieVar5):
        print ('1'+movieVar1)
    if movieVar2 in (movieVar1, movieVar3, movieVar4, movieVar5):
        print ('2'+movieVar2)
    if movieVar3 in (movieVar2, movieVar1, movieVar4, movieVar5):
        print ('3'+movieVar3)
    if movieVar4 in (movieVar2, movieVar3, movieVar1, movieVar5):
        print ('4'+movieVar4)
    if movieVar5 in (movieVar2, movieVar3, movieVar4, movieVar1):
        print ('5'+movieVar5)

print (findDupes())
