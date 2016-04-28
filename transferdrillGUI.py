import shutil
import os.path
from datetime import *

# Path to each folder
pathA =  os.path.expanduser('~\Desktop\Customer Orders')
pathB =  os.path.expanduser('~\Desktop\Home Office')

# Number of files in Customer Orders
numA = len([f for f in os.listdir(pathA)if os.path.isfile(os.path.join(pathA, f))])

# Today - 24 hours = "yesterday"
yesterday = datetime.now() - timedelta(days=1)

def main():
    start()

def modTime(filePath):
    t = os.path.getmtime(filePath)
    return datetime.fromtimestamp(t)

def start():
    
    # If there are no files in the folder, let user know
    if numA == 0:
        print "There are no files in Customer Orders."
        
    # Opening prompt
    else:
        choice = raw_input("You currently have "+str(numA)+
                           " file(s) in Customer Orders. "
                           "Would you like to move the new ones to Home Office? y/n: ")
        
        if choice == "y":
            
            # Figure out when each file in Customer Orders was modified
            for file in os.listdir(pathA):
                mod = modTime(pathA+"//"+file)

                # Copy the files that were modified in the last 24 hours
                if yesterday < mod:
                    shutil.copy((pathA+"//"+file), pathB)
                    print pathA+"//"+file+" successfully copied."

                # Ignore older files
                elif yesterday > mod:
                    print "File skipped."
                    
            print "Operation completed."
    
        else:
            print "OK, bye."

def counting():
    count = 0
    # Figure out how many files are new
    for file in os.listdir(pathA):
        mod = modTime(pathA+"//"+file)

        if yesterday < mod:
            count = count+1

    print count
            
counting()
start()
