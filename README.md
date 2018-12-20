# eBPF Instruction Converter
A simple and useful eBPF instruction converter for it equivalent code in machine language.

## Usage
Use `./ebpf_ic.py` with the following parameters to get a file (in the desired extension) with the correspondent code in machine language.

### Available parameters

| Parameter | Description |
| --- | --- |
| --bin | Generates machine language output code in binary |
| --hex | Generates machine language output code in hexadecimal |
| --apart | Generates two values (high and low, separated by a char) as the final instruction |
| --unique | Generates a single value as the final instruction |

### Usage example

> ./ebpf_ic.py --bin --unique input.txt output.txt
