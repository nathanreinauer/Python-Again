
epic_prog_dict = {"tim berners-lee":["tbl@gmail.com", 111],
                  "guido van rossum":["gvr@gmail.com", 222],
                  "linus torvalds":["lt@gmail.com", 333],
                  "larry page":["lp@gmail.com", 444],
                  "sergey brin":["sb@gmail.com", 555]
                  }

def searchPeople(personsName):
    
    try:
        personsInfo = epic_prog_dict[personsName]
        print "Name: " + personsName.title()
        print "Email: " + personsInfo[0]
        print "Number: " + str(personsInfo[1])
        
    except:
        print "No information found for that name."

userWantsMore = True

while userWantsMore == True:
    personsName = raw_input("Please enter a name: ").lower()
    searchPeople(personsName)
    searchAgain = raw_input("Search again? (Y or N)")
    if searchAgain == "Y":
        userWantsMore = True
    elif searchAgain == "N":
        print "Okay, all done."
        userWantsMore = False
    else:
        print "I don't understand. Quitting."
        userWantsMore = False

        
    
