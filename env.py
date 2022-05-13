def address(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")

def balance(cpu):
    cpu.stack.push(0xFF)

def origin(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")

def caller(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")

def callvalue(cpu):
    cpu.stack.push(0x00)

def calldataload(cpu):
    i = cpu.stack.pop()
    cpu.stack.push(0x00)

def calldatasize(cpu):
    cpu.stack.push(0x00)

def calldatacopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()
    # TODO: copy to memory

def codesize(cpu):
    cpu.stack.push(0x00)

def codecopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()
    # TODO: copy to memory
