def shl(cpu): 
    shift, value = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(value << shift)
    cpu.pc += 1
    cpu.gas_dec(3)

def shr(cpu): 
    shift, value = cpu.stack.pop().value, cpu.stack.pop().value
    cpu.stack.push(value >> shift)
    cpu.pc += 1
    cpu.gas_dec(3)
