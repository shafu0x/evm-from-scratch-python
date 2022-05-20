from ethereum.opcodes import *

def jump(cpu):
    counter = cpu.stack.pop().value

    # make sure that we jump to an JUMPDEST opcode
    if not cpu.program[counter] == JUMPDEST:
        raise Exception("Can only jump to JUMPDEST")

    cpu.pc = counter
    cpu.gas_dec(8)

def jumpi(cpu):
    counter, b = cpu.stack.pop().value, cpu.stack.pop().value

    if b != 0: cpu.pc = counter
    else     : cpu.pc += 1
    
    cpu.gas_dec(10)

def pc(cpu):
    cpu.stack.push(cpu.pc)
    cpu.pc += 1
    cpu.gas_dec(2)

def jumpdest(cpu):
    cpu.pc += 1
    cpu.gas_dec(1)
