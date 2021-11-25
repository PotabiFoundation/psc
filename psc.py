#!/bin/python3
import sys
import os
# If debugging is ever needed: 
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

base_commands=["clone","pull","commit","push","whoami"]

if len(sys.argv) < 2:
    exit

# Check if command is valid
def checkcommand(command,position):
    for i in base_commands:
        if (str(command) == str(i)):
            scmrun(str(i),int(position))
        else:
            exit

def scmrun(command,position):
    if(command == "commit"):
        # psc commit <dir> "message" push
        if len(sys.argv) < 4:
            exit
        else:
            directory = sys.argv[int(int(position)+1)]
            message   = sys.argv[int(int(position)+2)]

            print("Committing `" + str(directory) + "` with message `" + str(message) + "`")
            os.system("git add " + str(directory))
            os.system("git commit -m \"" + str(message) + "\"")

        # If there are any other arguments
        if len(sys.argv) >= 5:
            checkcommand(str(sys.argv[4]),int(4))
    elif(command == "clone"):
        # pcs clone <url> branch <branch>
        url = sys.argv[int(int(position)+1)]
        print("git clone " + url)
    elif(command == "pull"):
        pass
    elif(command == "push"):
        if int(int(position)+1) == len(sys.argv):
            pass
            os.system("git push")
        else:
            if int(len(sys.argv) - int(int(position)+1)) == int(2):
                remote = str(sys.argv[int(int(position)+1)])
                branch = str(sys.argv[int(int(position)+2)])
                os.system("git push " + remote + " " + branch)
            else:
                exit
    elif(command == "whoami"):
        def whoami_error():
            print("ERROR: whoami was not run properly")
            print("The Whoami function needs to be ran independently")
            print("Usage: psc whoami <global/local> <name> <email>")
            print("\tglobal: Set this to be for all repositories")
            print("\tlocal: Set this only for this repository")
            exit
        if int(position) is not int(1):
            whoami_error()
        elif int(len(sys.argv)) < 4 or int(len(sys.argv)) > 5:
            whoami_error()
        else:
            if str(sys.argv[int(int(position)+1)]) == str("global"):
                os.system("git config --global user.name " + str(sys.argv[int(int(position)+2)]))
                os.system("git config --global user.email " + str(sys.argv[int(int(position)+2)]))
                print("Success")
            elif str(sys.argv[int(int(position)+1)]) == str("local"):
                os.system("git config user.name " + str(sys.argv[int(int(position)+2)]))
                os.system("git config user.email " + str(sys.argv[int(int(position)+2)]))
                print("Success")
            else:
                whoami_error()

checkcommand(str(sys.argv[1]),int(1))