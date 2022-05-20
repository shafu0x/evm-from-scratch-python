def sload(cpu): 
    key = cpu.stack.pop().value
    warm, value = cpu.storage.load(key)
    cpu.stack.push(value)

    cpu.gas_dec(100 if warm else 2100)
    cpu.pc += 1

def sstore(cpu): 
    key, value = cpu.stack.pop().value, cpu.stack.pop().value
    warm, old_value = cpu.storage.store(key, value)

    base_dynamic_gas = 0

    # TODO: test
    if value != old_value:
        if old_value == 0:
            base_dynamic_gas = 20000
        else:
            base_dynamic_gas = 2900

    access_cost = 100 if warm else 2100
    cpu.gas_dec(base_dynamic_gas + access_cost)

    cpu.pc += 1

    # TODO: do refunds

