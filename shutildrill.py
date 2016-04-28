import shutil
import os.path


# number of files in folder A and B
pathA =  os.path.expanduser('~\Desktop\Folder A')#os.getenv('HOME') + '\Desktop\Folder A'
numA = len([f for f in os.listdir(pathA)if os.path.isfile(os.path.join(pathA, f))])

pathB =  os.path.expanduser('~\Desktop\Folder B')#os.getenv('HOME') + '\Desktop\Folder B'
numB = len([f for f in os.listdir(pathB)if os.path.isfile(os.path.join(pathB, f))])

def main():
    start()

def start():
    choice = raw_input("You currently have "+str(numA)+
                       " file(s) in Folder A. Would you like to move them to Folder B? y/n: ")
    if choice == "y":
        print str(pathA)
        for fileA in str(pathA):
            shutil.move(fileA, str(pathB))
    else:
        print "OK, bye."

    





















start()
