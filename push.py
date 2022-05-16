def _push(cpu, n):
    for _ in range(n): cpu.stack.push(cpu.peek())
    cpu.pc += n+1
