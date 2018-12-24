from data import *

def validateArgs(args):

    # Initial verifications:
    del args[0]
    if len(args) == 0:
        helpArgs(); return None
    elif len(args) < 2:
        print("ebpf_ic: error: not enough arguments"); return None

    # Initial info dictionary:
    backArgs = {
        'hexadecimal': True, 'aparted': True,
        'inputFile': '', 'outputFile': ''
    }

    # Filtering parameters by class:
    parameters = list(filter(lambda x: x.startswith('--'), args))
    files = list(filter(lambda x: x not in parameters, args))

    # Identifying parameters:
    for p in parameters:
        if p in args_set['data']:
            backArgs['hexadecimal'] = args_set['data'][p]['value']
        elif p in args_set['instruction']:
            backArgs['aparted'] = args_set['instruction'][p]['value']
        else:
            print("ebpf_ic: error: unknown parameter: " + p)
            helpArgs()
            return None

    # Identifying in/out files:
    for p in files:
        if p.find(".") == -1:
            print("ebpf_ic: error: invalid argument: " + p)
            return None

    backArgs['inputFile'] = files[0]
    backArgs['outputFile'] = files[1]

    # Return a dictionary with all the informations:
    return backArgs

def helpArgs():
    print("usage: ebpf_ic.py [--hex] [--bin] [--apart] [--unique] [input.ext] [output.ext]")
    print("       where:")
    for a in args_set:
        for b in args_set[a]:
            print("       " + b + ': ' + args_set[a][b]['description'])

    print("\nor use: ebpf_ic.py [input.ext] [output.ext]")
    print("        in this case, --hex and --apart are asserted by default.")
