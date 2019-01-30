# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *  File:
# *        main.py
# *
# *  Library:
# *        ebpf_ic/
# *
# *  Author:
# *        Lucas Duarte (lucas.f.duarte@ufv.br)
# *
# *  Description:
# *        Main file
# *

from engine import *
from data import *
from file import *
from args import *
from lib import *

def processInstructions(inputFile):
    """
    Receives instructions from an external input file and send it to translation.

    Args:
        inputFile: external input file.

    Returns:
        machineCode: a list with all the translated instructions in binary
        machine code.

    Raises:
        None
    """

    machineCode = []
    # Get all the instructions from external file:
    instructions = readFromFile(inputFile)

    for index, instruction in enumerate(instructions):

        # Checking for comments or empty lines:
        if instruction.startswith("//") or len(instruction) == 0: continue

        # Preparing instruction to be translated:
        instruction = instruction.replace(',', '')
        instruction = instruction.lower()

        # Define all the args (operation and parameters):
        a = instruction.split(' ')
        args = list(filter(lambda x: len(x) != 0, a))
        op = args[0]
        del args[0]

        # Execute the search and translation:
        if op in instr_set:
            machineCode.append(instr_set[op](op, args, index + 1))
        else: print("ebpf_ic: line " + str(index + 1) + ": unknown instruction")

    return machineCode

def writeInstructions(info, machineCode):
    """
    Prepare all the instructions based on the arguments and send it to be written.

    Args:
        info: parameters obtained from command line;
        machineCode: data to be analyzed and written.

    Returns:
        boolean: true if the data could be written; false if not.

    Raises:
        None
    """

    charApart = ' '
    finalMachineCode = []
    apart = info['aparted']
    hexa = info['hexadecimal']

    # Verify data integrity then send data to be written:
    if not None in machineCode:

        # --apart and --hex:
        if apart and hexa:
            for inst in machineCode:
                i = []
                i.append(inst[0:32])
                i.append(inst[32:])
                finalMachineCode.append(transformHex(i[0]) + charApart + transformHex(i[1]))

        # --apart and --bin:
        elif apart and not hexa:
            for inst in machineCode:
                finalMachineCode.append(apartInstruction(inst, charApart))

        # --unique and --hex:
        elif not apart and hexa:
            for inst in machineCode:
                finalMachineCode.append(transformHex(inst))

        # --unique and --bin:
        elif not apart and not hexa:
            for inst in machineCode:
                finalMachineCode = machineCode

        writeOnFile(finalMachineCode, info['outputFile'])
        return True
    else: return False
