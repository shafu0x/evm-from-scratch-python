def twos_comp(val, bits=256):
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val  

def to32(value):
    # if only one byte is passed
    if type(value) == int:
        value = [value]

    if len(value) < 32:
        while len(value) < 32:
            value.insert(0, 0x00)

    return value
