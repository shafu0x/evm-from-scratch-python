def address(cpu):
    cpu.stack.push("0xD912bCb457Ea4FB70EEAD8cfbbb97a32319e4dC7")
    cpu.pc += 1
    cpu.gas_dec(3)

def balance(cpu):
    # TODO: add address to cache
    address = cpu.stack.pop()

    def get_address_balance(address):
        return 0xFF

    # TODO: get balance of address
    cpu.stack.push(get_address_balance(address))

    cpu.pc += 1
    cpu.gas_dec(100 if address in cpu.address_cache else 2600)

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
    destOffset = cpu.stack.pop().value
    offset = cpu.stack.pop().value
    size = cpu.stack.pop().value

    calldata = cpu.calldata[offset:offset+size]
    memory_expansion_cost = cpu.memory.store(destOffset, calldata)

    static_gas = 3
    minimum_word_size = (size + 31) // 32
    dynamic_gas = 3 * minimum_word_size + memory_expansion_cost
    cpu.gas_dec(static_gas + dynamic_gas)
    cpu.pc += 1

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

    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size # TODO: + memory_expansion_cost
    cpu.gas_dec(3 + dynamic_gas)

def gasprice(cpu):
    cpu.stack.push(0x00)
    cpu.pc += 1
    cpu.gas_dec(2)

def extcodesize(cpu):
    # TODO: add address to cache
    address = cpu.stack.pop()

    # TODO
    def get_address_codesize(address):
        return 0xFF

    cpu.stack.push(get_address_codesize(address))

    cpu.pc += 1
    cpu.gas_dec(100 if address in cpu.address_cache else 2600)

def extcodecopy(cpu):
    address = cpu.stack.pop()
    destOffset = cpu.stack.pop()
    offset = cpu.stack.pop()
    size = cpu.stack.pop()

    cpu.pc += 1

    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size # TODO: + memory_expansion_cost
    address_access_cost = 100 if address in cpu.address_cache else 2600
    cpu.gas_dec(0 + dynamic_gas + address_access_cost)

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

    minimum_word_size = (size + 31) / 32
    dynamic_gas = 3 * minimum_word_size # TODO: + memory_expansion_cost
    cpu.gas_dec(3 + dynamic_gas)


def extcodehash(cpu):
    address = cpu.stack.pop()

    def get_address_code_hash(address):
        # TODO: check if EOA or not
        return 0xFF

    cpu.stack.push(get_address_code_hash(address))

    cpu.pc += 1
    cpu.gas_dec(100 if address in cpu.address_cache else 2600)

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
