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
    if numA == 0:
        print "There are no files in Folder A."
        exit()
    else:
        choice = raw_input("You currently have "+str(numA)+
                           " file(s) in Folder A. Would you like to move them to Folder B? y/n: ")
        if choice == "y":
            for file in os.listdir(pathA):
                shutil.move((pathA+"//"+file), pathB)
                print pathA+"//"+file+" successfully moved."
            print "Operation completed."
        else:
            print "OK, bye."
            exit()


start()
