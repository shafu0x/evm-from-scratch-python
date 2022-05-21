from utils import *
from ethereum.number import *

# protect from under-overflow
# always stay at 32 bytes!
def protect(value):
    if   value < 0       : return value + MAX_UINT       # handle underflow
    elif value > MAX_UINT: return 0 + (value - MAX_UINT) # handle overflow
    else                 : return value % MAX_UINT       # just to be sure           

def add(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(protect(a+b))
    cpu.pc += 1
    cpu.gas_dec(3)

def mul(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(protect(a*b))
    cpu.pc += 1
    cpu.gas_dec(5)

def sub(cpu):
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(protect(a-b))
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
    a, b = cpu.stack.pop().value, cpu.stack.pop().value
    N = cpu.stack.pop().value
    print("addmod:", a,b,N)
    cpu.stack.push(protect(a + b) % N)
    cpu.pc += 1
    cpu.gas_dec(8)

def mulmod(cpu):
    a, b, N = cpu.stack.pop().value, cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(protect(a + b) * N)
    cpu.pc += 1
    cpu.gas_dec(8)

def exp(cpu):
    a, exponent = cpu.stack.pop().value, cpu.stack.pop()
    cpu.stack.push(protect(a ** exponent.value))
    cpu.pc += 1
    cpu.gas_dec(10 + (50 * len(exponent.bytes)))

# TODO
def signextend(cpu):
    b, x = cpu.stack.pop().value, cpu.stack.pop().value


