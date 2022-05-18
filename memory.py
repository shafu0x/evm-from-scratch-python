class Memory:
    def __init__(self):
        self.memory = []

    def access(self, offset, size): return self.memory[offset:offset+size]

    def store(self, offset, value):
        memory_expansion_cost = 0

        # increase memory if not enough available
        if len(self.memory) <= offset:

            expansion_size = 0

            # init memory if memory is empty
            if len(self.memory) == 0:
                expansion_size = expansion_size + 32
                self.memory = [0x00 for _ in range(32)]

            # extend memory if needed
            if len(self.memory) - offset < 0:
                expansion_size += offset - len(self.memory)
                self.memory.append(0x00 * expansion_size)

            # calc memory expansion gas cost
            memory_expansion_cost = self.calc_memory_expansion_gas(expansion_size)

        self.memory[offset:len(value)] = value
        return memory_expansion_cost

    def load(self, offset):
        value = self.memory[offset:offset+32]
        if len(value) < 32: raise Exception("mload: Not 32 Bytes")

        return value

    def calc_memory_expansion_gas(self, memory_byte_size):
        memory_size_word = (memory_byte_size + 31) / 32
        memory_cost = (memory_size_word ** 2) / 512 + (3 * memory_size_word)
        return round(memory_cost)

class ROM:
    pass
