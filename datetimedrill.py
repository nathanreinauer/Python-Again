import datetime

portlandInt = int(datetime.datetime.now().strftime("%H%M"))
newyorkInt = int(datetime.datetime.now().strftime("%H%M")) + 300
londonInt = int(datetime.datetime.now().strftime("%H%M")) + 800

def main():
    start()

def start():
    choice = raw_input("To check if a branch is open, type 'p' for Portland, 'n' for New York, and 'l' for London.")

    if choice == "p":
        q = portlandInt
        c = "Portland"
    elif choice == "n":
        q = newyorkInt
        c = "New York"
    elif choice == "l":
        q = londonInt
        c = "London"
    else:
        print "Input not recognized. Please try again."
        start()

    if q < 900 or q > 2100:
        a = False
    else:
        a = True

    def answer():
        if a == True:
            print "Yes, our "+c+" branch is open!"
        else:
            print "Sorry, our "+c+" branch is currently closed."

    answer()
    start()
    
start()
