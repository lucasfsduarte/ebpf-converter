from lib import *
from data import *
from file import *
from args import *
from engine import *

def processInstructions(inputFile):

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
        args = instruction.split(' ')
        op = args[0]
        del args[0]

        # Execute the search and translation:
        if op in instr_set:
            machineCode.append(instr_set[op](op, args, index + 1))
        else: print("ebpf_ic: line " + str(index + 1) + ": unknown instruction")

    return machineCode

def writeInstructions(info, machineCode):

        # Verify data integrity then send data to be written:
        if not None in machineCode:
            # If the parameter --apart is active:
            if info['instructionType'] == 0:
                apartedMachineCode = []
                for instruction in machineCode:
                    apartedMachineCode.append(apartInstruction(instruction, ','))
                writeOnFile(apartedMachineCode, info['outputFile'])
            else:
                writeOnFile(machineCode, info['outputFile'])
            return True
        else: return False
