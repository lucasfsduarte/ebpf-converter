# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *  File:
# *        file.py
# *
# *  Library:
# *        ebpf_ic/
# *
# *  Author:
# *        Lucas Duarte (lucas.f.duarte@ufv.br)
# *
# *  Description:
# *        Write from and read into files methods
# *

from lib import *

def writeOnFile(data, destiny):
    """
    Writes data into a predefined output file.

    Args:
        data: data to be written;
        destiny: output file path.

    Returns:
        None

    Raises:
        None
    """

    file = open(destiny, "w")
    file.write(transformHex(completeBinary(bin(len(data)), 32)) + '\n')
    for line in data:
        file.write(line + '\n')
    file.close()

def readFromFile(origin):
    """
    Reads data from a predefined input file.

    Args:
        origin: input file path.

    Returns:
        None

    Raises:
        None
    """

    file = open(origin, "r")
    data = file.readlines()
    for i in range(0, len(data)): data[i] = data[i].replace('\n', '')
    file.close()
    return data if len(data) > 0 else None
