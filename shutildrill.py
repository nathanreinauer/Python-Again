import shutil
import os.path


# number of files in folder A and B
path = os.getenv('HOME') + '\Desktop\Folder A'
numA = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

path = os.getenv('HOME') + '\Desktop\Folder B'
numB = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

def main():
    start()

def start():
    choice = raw_input("You currently have "+str(numA)+
                       " files in Folder A. Would you like to move them to Folder B? y/n: ")

    





















start()
