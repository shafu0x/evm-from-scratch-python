class Log:
    def __init__(self, data, topic1=None, topic2=None, topic3=None, topic4=None):
        self.data = data
        self.topic1 = topic1
        self.topic2 = topic2
        self.topic3 = topic3
        self.topic4 = topic4

    def __str__(self): return f"Log: {self.data}"

def log0(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value

    data = cpu.memory.access(offset, size)
    log = Log(data)
    cpu.append_log(log)

    cpu.pc += 1
    # TODO: dynamic cost
    cpu.gas_dec(375)

def log1(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value
    topic = cpu.stack.pop().value

    data = cpu.memory.access(offset, size)
    log = Log(data, topic)
    cpu.append_log(log)

    cpu.pc += 1
    # TODO: dynamic cost
    cpu.gas_dec(750)

def log2(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value
    topic1, topic2 = cpu.stack.pop().value, cpu.stack.pop().value

    data = cpu.memory.access(offset, size)
    log = Log(data, topic1, topic2)
    cpu.append_log(log)

    cpu.pc += 1
    # TODO: dynamic cost
    cpu.gas_dec(1125)

def log3(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value
    topic1 = cpu.stack.pop().value
    topic2 = cpu.stack.pop().value
    topic3 = cpu.stack.pop().value

    data = cpu.memory.access(offset, size)
    log = Log(data, topic1, topic2, topic3)
    cpu.append_log(log)

    cpu.pc += 1
    # TODO: dynamic cost
    cpu.gas_dec(1500)

def log4(cpu):
    offset, size = cpu.stack.pop().value, cpu.stack.pop().value
    topic1 = cpu.stack.pop().value
    topic2 = cpu.stack.pop().value
    topic3 = cpu.stack.pop().value
    topic4 = cpu.stack.pop().value

    data = cpu.memory.access(offset, size)
    log = Log(data, topic1, topic2, topic3, topic4)
    cpu.append_log(log)

    cpu.pc += 1
    # TODO: dynamic cost
    cpu.gas_dec(1875)
