class Memory:
    def __init__(self):
        self.memory = []

    def access(self, offset, size): return self.memory[offset:offset+size]

    def store(self, offset, value):
        # init memory
        if len(self.memory) == 0:
            self.memory = [0x00 for _ in range(32)]

        # increase memory if not enough available
        if len(self.memory) < offset:
            while len(self.memory) < offset:
                self.memory.append(0x00)

        self.memory[offset:len(value)] = value

    def load(self, offset):
        value = self.memory[offset:offset+32]
        if len(value) < 32: raise Exception("mload: Not 32 Bytes")

        return value

class ROM:
    pass
