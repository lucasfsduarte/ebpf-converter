from lib import *

def writeOnFile(data, destiny):
    from lib import transformHex
    file = open(destiny, "w")
    file.write(transformHex(completeBinary(bin(len(data)), 32)) + '\n')
    for line in data:
        file.write(line + '\n')
    file.close()

def readFromFile(origin):
    file = open(origin, "r")
    data = file.readlines()
    # Remove '\n' from the line:
    for i in range(0, len(data)): data[i] = data[i].replace('\n', '')
    file.close()
    return data if len(data) > 0 else None
