def _push(cpu, n):
    cpu.pc += 1
    cpu.gas_dec(3)

    value = []
    for _ in range(n): 
        value.append(cpu.peek())
        cpu.pc += 1
    cpu.stack.push(value)
