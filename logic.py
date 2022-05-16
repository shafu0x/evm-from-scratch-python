def _and(cpu):
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(a & b)
    cpu.pc += 1
    cpu.gas_dec(3)

def _or(cpu): 
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(a | b)
    cpu.pc += 1
    cpu.gas_dec(3)

def _xor(cpu): 
    a, b = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(a ^ b)
    cpu.pc += 1
    cpu.gas_dec(3)

def _not(cpu): 
    a = cpu.stack.pop()
    cpu.stack.push(~a)
    cpu.pc += 1
    cpu.gas_dec(3)
