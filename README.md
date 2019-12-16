# eBPF Instruction Converter
A complete eBPF to machine code converter.

## Usage
Use `./ebpf_ic.py` with the following parameters to get a file (in the desired extension) with the correspondent code in machine language.

### Available parameters

| Parameter | Description |
| --- | --- |
| --bin | Generates machine language output code in binary |
| --hex | Generates machine language output code in hexadecimal |
| --apart | Generates two values (high and low, 32 bits each one, separated by a char) as the final instruction |
| --unique | Generates a single value (64 bits) as the final instruction |

### Usage

`./ebpf_ic.py --hex --apart input.txt output.txt`

### How results looks like

1. Using `--hex` and `--apart`

**input:** `add r0, 0x20`; **output:** `0x14, 0x7`

2. Using `--hex` and `--unique`

**input:** `add r0, 0x20`; **output:** `0x0000002000000007`

### Syntax

The acceptable syntax is very simple. The operations can be written both in lowercase and uppercase. The registers can be written using the letter `r` to sinalize it, and the numbers can be written in decimal, binary and hexadecimal. However, there should be some prefixes used to indicate the current basis. By default, binary numbers should be represented after the prefix `0b` and hexadecimal numbers should be represented after `0x`. Decimal numbers do not need any prefix. Moreover, numbers can be negative numbers. All needed to represent negative numbers is to acrescent a `-` signal before the whole number.

### Syntax example

> mov r2, -0x4AF

> add r2, r5

> add r2, 104

> add r4, 0b1011

> sub r4, r2

> exit
