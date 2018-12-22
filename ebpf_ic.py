#!/usr/bin/env python3

import sys

# Insert ebpf_ic folder on the path:
sys.path.insert(0, './ebpf_ic')

from data import *
from args import *
from file import *
from main import *

info = validateArgs(sys.argv)
machineCode = processInstructions(info['inputFile'])
writeInstructions(info, machineCode)
