#!/usr/bin/env python3

import sys

# Insert ebpf_ic folder on the path:
sys.path.insert(0, './ebpf_ic')

from data import *
from args import *
from file import *

data = ["lucas\n", "lucas\n", "lucas\n", "10\n"]

info = validateArgs(sys.argv)
writeOnFile(data, info['outputFile'])
readFromFile(info['inputFile'])
