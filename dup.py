def _dup(cpu, n):
    value = cpu.stack[n]
    cpu.stack.push(value)

    cpu.pc += 1
    cpu.gas_dec(3)

