import os.path
from os import path
from os import stat

def pathChecker(path):
    matchingElement = False
    breakOutFlag = False

    if os.path.exists(path):
        os.chdir(path)
        for file in os.listdir(path):
            if file.endswith(".exe"):
                if int((os.stat(file).st_size/1048576)) < 14:
                    if os.stat(file).st_uid == 0:
                        matchingElement = True
                        breakOutFlag = True
                        break
            if breakOutFlag == True:
                break

    return matchingElement