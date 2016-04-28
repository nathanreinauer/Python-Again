import shutil
import os.path
from datetime import *

# number of files in folder A and B
pathA =  os.path.expanduser('~\Desktop\Folder A')
numA = len([f for f in os.listdir(pathA)if os.path.isfile(os.path.join(pathA, f))])

pathB =  os.path.expanduser('~\Desktop\Folder B')
numB = len([f for f in os.listdir(pathB)if os.path.isfile(os.path.join(pathB, f))])

def main():
    start()
    
def start():
    if numA == 0:
        print "There are no new files in Customer Orders."
        exit()
    else:
        choice = raw_input("You currently have "+str(numA)+
                           " new file(s) in Customer Orders. "
                           "Would you like to move them to Home Office? y/n: ")
        if choice == "y":
            for file in os.listdir(pathA):
                shutil.copy((pathA+"//"+file), pathB)
                print pathA+"//"+file+" successfully copied."
            print "Operation completed."
        else:
            print "OK, bye."
            exit()
            
yesterday = datetime.now() - timedelta(days=1)
print yesterday

def modTime(filePath):
    t = os.path.getmtime(filePath)
    return datetime.fromtimestamp(t)

for file in os.listdir(pathA):
    d = modTime(pathA+"//"+file)
    if yesterday > d:
        print "yes"
        shutil.copy((pathA+"//"+file), pathB)
        print pathA+"//"+file+" successfully copied."
    if yesterday < d:
        print "no"




start()
