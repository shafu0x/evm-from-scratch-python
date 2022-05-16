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
    cpu.gas_dec(2)

def caller(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1
    cpu.gas_dec(2)

def callvalue(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def calldataload(cpu):
    i = cpu.stack.pop()
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(3)

def calldatasize(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def calldatacopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()
    # TODO: copy to memory
    cpu.pc += 1
    # TODO: dynamic stuff
    cpu.gas_dec(3)

def codesize(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def codecopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()
    # TODO: copy to memory
    cpu.pc += 1
    cpu.gas_dec(3)

def gasprice(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def extcodesize(cpu):
    cpu.stack.push(0xFF)
    cpu.pc += 1
    # TODO: dynamic stuff
    cpu.gas_dec(100)

def extcodecopy(cpu):
    address = cpu.stack.pop()
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()

    cpu.pc += 1
    # TODO: dynamic stuff
    cpu.gas_dec(100)

def returndatasize(cpu):
    cpu.stack.push(0xFF)
    cpu.pc += 1
    # TODO: dynamic stuff
    cpu.gas_dec(100)

def returndatacopy(cpu):
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()

    cpu.pc += 1
    cpu.gas_dec(3)

def extcodehash(cpu):
    address = cpu.stack.pop()

    cpu.pc += 1
    cpu.gas_dec(100)

def blockhash(cpu):
    blockNumber = cpu.stack.pop().value
    if blockNumber > 256: raise Exception("blockhash: Only last 256 blocks can be accessed")
    cpu.stack.push(0x1cbcfa1ffb1ca1ca8397d4f490194db5fc0543089b9dee43f76cf3f962a185e8)

    cpu.pc += 1
    cpu.gas_dec(20)

def coinbase(cpu):
    # address of miner
    cpu.stack.push(0x1cbcfa1ffb1ca1ca8397d4f490194db5fc0543089b9dee43f76cf3f962a185e8)

    cpu.pc += 1
    cpu.gas_dec(2)
