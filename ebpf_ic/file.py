
def writeOnFile(data, destiny):
    file = open(destiny, "w")
    file.write(str(len(data)) + '\n')
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
