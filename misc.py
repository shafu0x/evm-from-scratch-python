from number import *
from eth_hash.auto import keccak

def sha3(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value
    value = cpu.memory.access(offset, size)
    cpu.stack.push(keccak(value))

    cpu.pc += 1
    # TODO
    cpu.gas_dec(30)
