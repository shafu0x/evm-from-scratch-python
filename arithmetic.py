from utils import *
from number import *

# TODO: check for overflow
def add(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a + b)
    cpu.pc += 1
    cpu.gas_dec(3)

def mul(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a * b)
    cpu.pc += 1
    cpu.gas_dec(5)

# TODO: check for underflow
def sub(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a - b)
    cpu.pc += 1
    cpu.gas_dec(3)

def div(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a // b)
    cpu.pc += 1
    cpu.gas_dec(5)

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

def exp(cpu):
    a, exponent = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a ** exponent)
    cpu.pc += 1
    cpu.gas_dec(8)
