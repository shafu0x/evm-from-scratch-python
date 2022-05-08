def lt(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(1 if a < b else 0)
    cpu.pc += 1

def gt(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(1 if a > b else 0)
    cpu.pc += 1

def eq(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(1 if a == b else 0)
    cpu.pc += 1

def iszero(cpu):
    a = cpu.stack.pop()
    cpu.stack.push(1 if a == 0 else 0)
    cpu.pc += 1
