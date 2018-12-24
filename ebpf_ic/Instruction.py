# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *  File:
# *        Instruction.py
# *
# *  Library:
# *        ebpf_ic/
# *
# *  Author:
# *        Lucas Duarte (lucas.f.duarte@ufv.br)
# *
# *  Description:
# *        Instruction class file
# *

class Instruction:

    def __init__(self):
        """
        Instruction class constructor method.

        Args:
            self

        Returns:
            None

        Raises:
            None
        """

        self.immediate = 32 * '0'
        self.offset = 16 * '0'
        self.src = 4 * '0'
        self.dst = 4 * '0'
        self.opcode = 8 * '0'

    # Get methods
    def getImm(self): return self.immediate
    def getOff(self): return self.offset
    def getSrc(self): return self.src
    def getDst(self): return self.dst
    def getOpc(self): return self.opcode

    # Set methods
    def setImm(self, imm): self.immediate = imm
    def setOff(self, off): self.offset = off
    def setSrc(self, src): self.src = src
    def setDst(self, dst): self.dst = dst
    def setOpc(self, opc): self.opcode = opc

    # ToString method
    def toString(self): return self.immediate + self.offset + self.src + self.dst + self.opcode
