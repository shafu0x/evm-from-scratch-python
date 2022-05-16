from utils import *

def byte(cpu):
    i, x = cpu.stack.pop().value, to32(cpu.stack.pop().bytes)
    try:    cpu.stack.push(x[i])
    except: cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(3)

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
