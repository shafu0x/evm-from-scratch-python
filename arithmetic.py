from utils import *
from number import *

# TODO: check for overflow
def add(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a + b)
    cpu.pc += 1

def mul(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a * b)
    cpu.pc += 1

# TODO: check for underflow
def sub(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a - b)
    cpu.pc += 1

def div(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a // b)
    cpu.pc += 1

def sdiv(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a // b)
    cpu.pc += 1

def mod(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a % b)
    cpu.pc += 1

def smod(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(0 if b == 0 else a % b)
    cpu.pc += 1

def addmod(cpu):
    a, b, N = cpu.stack.pop().value, cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push((a + b) % N)
    cpu.pc += 1

def exp(cpu):
    a, exponent = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(a ** exponent)
    cpu.pc += 1
