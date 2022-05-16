class Number:
    def __init__(self, value):
        self.bytes = value
        self.value = self.parse(value)

    def parse(self, value):
        if type(value) == list:
            return int.from_bytes(bytearray(value), "big", signed=False)
        return value

    def to_bytes(self):
        return [hex(a) for a in self.value.to_bytes(32, byteorder="big")]

    def __str__(self): return f"{self.value}"
