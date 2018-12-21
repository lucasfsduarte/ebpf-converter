
def writeOnFile(data, destiny):
    file = open(destiny, "w")
    for line in data:
        file.write(line)
    file.close()

def readFromFile(origin):
    file = open(origin, "r")
    data = file.readlines()
    # Remove '\n' from the line:
    for i in range(0, len(data)): data[i] = data[i].replace('\n', '')
    file.close()
    return data if len(data) > 0 else None
