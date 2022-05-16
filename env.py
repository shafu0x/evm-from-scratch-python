def address(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1
    cpu.gas_dec(3)

def balance(cpu):
    cpu.stack.push(0xFF)
    cpu.pc += 1

    # TODO: dynamic stuff
    cpu.gas_dec(100)

def origin(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1

def caller(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1

def callvalue(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1

def calldataload(cpu):
    i = cpu.stack.pop()
    cpu.stack.push(0x00)
    cpu.pc += 1

def calldatasize(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1

def calldatacopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()
    # TODO: copy to memory
    cpu.pc += 1

def codesize(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1

def codecopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()
    # TODO: copy to memory
    cpu.pc += 1
