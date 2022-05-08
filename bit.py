def shl(cpu): 
    shift, value = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(value << shift)

def shr(cpu): 
    shift, value = cpu.stack.pop(), cpu.stack.pop()
    cpu.stack.push(value >> shift)
