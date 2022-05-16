class Number:
    def __init__(self, value):
        self.value = self.parse(value)

    def parse(self, value):
        if type(value) == list:
            return int.from_bytes(bytearray(value), "big", signed=False)
        return value

    def __add__(self, other):  return other.value +  self.value
    def __sub__(self, other):  return other.value -  self.value
    def __mul__(self, other):  return other.value *  self.value
    def __div__(self, other):  return other.value // self.value
    def __sdiv__(self, other): return other.value // self.value

    def to_bytes(self):
        return [hex(a) for a in self.value.to_bytes(32, byteorder="big")]

    def __str__(self): return f"{self.value}"
