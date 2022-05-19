from number import *
from eth_hash.auto import keccak

def sha3(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value
    value = cpu.memory.access(offset, size)
    cpu.stack.push(keccak(value))

    cpu.pc += 1

    # calculate gas
    minimum_word_size = (size + 31) / 32
    dynamic_gas = 6 * minimum_word_size # TODO: + memory_expansion_cost
    cpu.gas_dec(30 + dynamic_gas)

def selfdestruct(cpu):
    address = cpu.stack.pop().value

    # TODO: send address all the balance
    # something with cpu.balance

    cpu.stop_flag = True
    cpu.pc += 1
    cpu.gas_dec(5000)

def _return(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.returndata = cpu.memory.access(offset, size)

    cpu.stop_flag = True
    cpu.pc += 1
    cpu.gas_dec(0)
