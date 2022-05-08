from utils import *

# TODO: check for overflow
def add(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(a + b)
    cpu.pc += 1


def mul(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append(a * b)
    cpu.pc += 1



# TODO: check for underflow
def sub(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append(a - b)
    cpu.pc += 1


def div(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append(0 if b == 0 else a // b)
    cpu.pc += 1


def sdiv(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append(0 if b == 0 else a // b)
    cpu.pc += 1


def mod(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append(0 if b == 0 else a % b)
    cpu.pc += 1


def smod(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append(0 if b == 0 else a % b)
    cpu.pc += 1


def addmod(cpu):
    a, b, N = cpu.stack.pop(), cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append((a + b) % N)
    cpu.pc += 1


def exp(cpu):
    a, exponent = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.append(a ** exponent)
    cpu.pc += 1
