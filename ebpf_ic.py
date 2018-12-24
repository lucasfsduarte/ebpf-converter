#!/usr/bin/env python3
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *  File:
# *        ebpf_ic.py
# *
# *  Library:
# *        ebpf_ic/
# *
# *  Author:
# *        Lucas Duarte (lucas.f.duarte@ufv.br)
# *
# *  Description:
# *        Script file responsible for receive all the parameters from
# *        command line and start the conversion proccess.
# *

import sys

# Insert ebpf_ic folder on the path:
sys.path.insert(0, './ebpf_ic')

from data import *
from args import *
from file import *
from main import *

info = validateArgs(sys.argv)
if info != None:
    machineCode = processInstructions(info['inputFile'])
    writeInstructions(info, machineCode)
