
# Valid arguments:
args_set = {

    'data': {
        '--hex':    {'description': 'Generates machine language in hexadecimal', 'value': 0},
        '--bin':    {'description': 'Generates machine language in binary', 'value': 1}
    },
    'instruction': {
        '--apart':  {'description': 'Generates two values (high and low) as the final instruction', 'value': 0},
        '--unique': {'description': 'Generates a single value as the final instruction', 'value': 1}
    }
}
