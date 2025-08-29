import os
import sys
#import time # to be used later

isDebug = True
prompt = "projman-0.1"
version = "0.1"

configDir = os.path.expanduser("~/.config/projman/")
def checkdir(path):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)
        if isDebug:
            print(f"File Created at {path}")
    else:
        return True

def projmanExit(): # future proof
    sys.exit()


def main():
    isRunning = True
    checkDirectory = checkdir(configDir)

    if checkDirectory:
        while isRunning:
            userInput = input("projman> ")
            if userInput == "new".lower():
                inputProjectName = input("Project Name: ").strip()
                inputProjectEditor = input("Project Editor: ").strip()
                inputProjectPath = input("Path (.): ").strip()
                inputProjectCI = input("Compiler/Interpreter: ").strip()

                filePath = os.path.join(configDir, inputProjectName)
                if os.path.exists(inputProjectPath):
                    with open(filePath, "w") as fw:
                        if inputProjectPath == "":
                            inputProjectPath = os.getcwd()

                            fw.write(f"Project: '{inputProjectName}'\n")
                            fw.write(f"Editor: '{inputProjectEditor}'\n")
                            fw.write(f"Path: '{inputProjectPath}'\n")
                            fw.write(f"Compiler/Interpreter: '{inputProjectCI}'")

                        if isDebug:
                            print(f"File '{inputProjectName}' Created")
                else:
                    pass


            elif userInput == "list".lower():
                files = os.listdir(configDir)
                if not files:
                    print("project not found")
                else:
                    print("Projects: (type 'show' to select a file) ")
                    for f in files:
                        print(f)

            elif userInput == "show".lower():
                afiles = os.listdir(inputProjectPath)
                if not afiles:
                    print("No projects were found!")
                else:
                    print("Projects: ")
                    with open(filePath, "a") as fr:
                        print(fr.read(100))


            elif userInput == "quit".lower():
                projmanExit()
            else:
                print("Unknown Command")


main()
