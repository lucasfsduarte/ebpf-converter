
def writeOnFile(data, destiny):
    file = open(destiny, "w")
    for line in data:
        file.write(line)
    file.close()

def readFromFile(origin):
    file = open(origin, "r")
    data = file.readlines()
    file.close()
    return data if len(data) > 0 else None
