import time
global gold
apples = 0
gold = 0

def start():
    print "Hello and welcome!"
    name = raw_input("What's your name:")
    print "Welcome,",name,"!"
    print "The objective of this game is to collect apples."
    print "After collecting the apples you sell them."
    choice = raw_input("Do you want to play? y/n")
    if choice == "y":
        print "Let's get started!"
        begin()
    if choice == "n":
        print "Okay, bye...."
        
def begin():
    global apples
    global gold
    if gold > 99:
        print "You've won the game!"
        play = raw_input("Wanna play again? y/n")
        if play == 'y':
            begin()
        if play == 'n':
            print "Congrats again!"
    pick = raw_input("Do you want to pick an apple? y/n")
    if pick == "y":
        time.sleep(1)
        print "You pick an apple."
        apples=apples+1
        print "You currently have",apples,"apples."
        begin()
    if pick == 'n':
        sell = raw_input("Do you want to sell your apples? y/n")
        if sell == 'y':
            global gold
            global apples
            print "You currently have",apples,"apples."
            print "You have sold your apples."
            gold=apples*10
            apples=0
            print "Your gold is now:",gold
            begin()
        if sell == 'n':
            last = raw_input("Do you want to keep playing? y/n")
            if last == "y":
                begin()
            if last == "n":
                print "Alright. See yeah."
                
start()
    
    
