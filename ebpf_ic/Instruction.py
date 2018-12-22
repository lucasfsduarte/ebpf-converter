class Instruction:
    def __init__(self):
        self.immediate = 32 * '0'
        self.offset = 16 * '0'
        self.src = 4 * '0'
        self.dst = 4 * '0'
        self.opcode = 8 * '0'

    def getImm(self): return self.immediate
    def getOff(self): return self.offset
    def getSrc(self): return self.src
    def getDst(self): return self.dst
    def getOpc(self): return self.opcode

    def setImm(self, imm): self.immediate = imm
    def setOff(self, off): self.offset = off
    def setSrc(self, src): self.src = src
    def setDst(self, dst): self.dst = dst
    def setOpc(self, opc): self.opcode = opc

    def toString(self): return self.immediate + self.offset + self.src + self.dst + self.opcode
