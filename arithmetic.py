from utils import *
from number import *

def add(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a + b % MAX_UINT)
    cpu.pc += 1
    cpu.gas_dec(3)

def mul(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a * b % MAX_UINT)
    cpu.pc += 1
    cpu.gas_dec(5)

def sub(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a - b % MAX_UINT)
    cpu.pc += 1
    cpu.gas_dec(3)

def div(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a // b)
    cpu.pc += 1
    cpu.gas_dec(5)

# TODO: overflow protection
def sdiv(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a // b)
    cpu.pc += 1
    cpu.gas -= 5
    cpu.gas_dec(5)

def mod(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a % b)
    cpu.pc += 1
    cpu.gas_dec(5)

def smod(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a % b)
    cpu.pc += 1
    cpu.gas_dec(5)

def addmod(cpu):
    a, b, N = cpu.stack.pop().value, cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push((a + b) % N)
    cpu.pc += 1
    cpu.gas_dec(8)

def mulmod(cpu):
    a, b, N = cpu.stack.pop().value, cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push((a + b) * N)
    cpu.pc += 1
    cpu.gas_dec(8)

def exp(cpu):
    a, exponent = cpu.stack.pop().value, cpu.stack.pop()
    cpu.stack.push(a ** exponent.value)
    cpu.pc += 1
    cpu.gas_dec(10 + (50 * len(exponent.bytes)))

# TODO
def signextend(cpu):
    b, x = cpu.stack.pop().value, cpu.stack.pop().value


