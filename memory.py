class Memory:
    def __init__(self):
        self.memory = []

    def store(self, offset, value):
        # init memory
        if len(self.memory) == 0:
            self.memory = [0x00 for _ in range(32)]

        # increase memory
        if len(self.memory) <= offset:
            while len(self.memory) <= offset:
                self.memory.append(0x00)

        self.memory[offset] = value

    def load(self):
        pass

