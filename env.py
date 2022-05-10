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
