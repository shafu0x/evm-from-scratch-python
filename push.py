def _push(cpu, n):
    for i in range(n): cpu.stack.push(cpu.peek())
    cpu.pc += n+1
