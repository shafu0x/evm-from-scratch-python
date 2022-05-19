def _swap(cpu, n):
    value1, value2 = cpu.stack.get(0), cpu.stack.get(n+1)
    cpu.stack.set(0, value2)
    cpu.stack.set(n+1, value1)

    cpu.pc += 1
    cpu.gas_dec(3)
