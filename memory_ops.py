from utils import *

def mstore8(cpu): 
    offset, value = cpu.stack.pop().value, cpu.stack.pop().bytes
    cpu.memory.store(offset, value)
    cpu.pc += 1

def mstore(cpu): 
    offset, value = cpu.stack.pop().value, cpu.stack.pop().bytes
    cpu.memory.store(offset, value)
    cpu.pc += 1

def mload(cpu): 
    offset = cpu.stack.pop().value
    value = cpu.memory.load(offset)
    cpu.stack.push(value)
    cpu.pc += 1
