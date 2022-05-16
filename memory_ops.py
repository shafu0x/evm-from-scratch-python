from utils import *

def mstore8(cpu): 
    offset, value = cpu.stack.pop(), cpu.stack.pop()
    cpu.memory.store(offset, value)
    cpu.pc += 1

def mstore(cpu): 
    offset, value = cpu.stack.pop(), to32(cpu.stack.pop())
    cpu.memory.store(offset, value)
    cpu.pc += 1

