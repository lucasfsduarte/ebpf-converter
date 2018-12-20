# eBPF Instruction Converter
A simple and useful eBPF instruction converter for it equivalent code in machine language.

## Usage
Use `./ebpf_ic.py` with the following parameters to get a file (in the desired extension) with the correspondent code in machine language.

### Available parameters

| Parameter | Description |
| --- | --- |
| --bin | Generates machine language output code in binary |
| --hex | Generates machine language output code in hexadecimal |
| --apart | Generates two values (high and low, 32 bits each one, separated by a char) as the final instruction |
| --unique | Generates a single value (64 bits) as the final instruction |

### Usage example

`./ebpf_ic.py --hex --apart input.txt output.txt`

### Results example

1. Using `--hex` and `--apart`

**input:** `add r0, 0x20`; **output:** `0x14, 0x7`

2. Using `--bin` and `--unique`

**input:** `add r0, 0x20`; **output:** `0000000000000000000000000001010000000000000000000000000000000111`
