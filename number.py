class Number:
    def __init__(self, value):
        self.value = self.parse(value)

    def parse(self, value):
        return int.from_bytes(bytearray(value), "big", signed=False)

    def __add__(self, other):  return self.to_list(other.value +  self.value)
    def __sub__(self, other):  return self.to_list(other.value -  self.value)
    def __mul__(self, other):  return self.to_list(other.value *  self.value)
    def __div__(self, other):  return self.to_list(other.value // self.value)
    def __sdiv__(self, other): return self.to_list(other.value // self.value)

    def to_list(self, a): return [a for a in a.to_bytes(32, byteorder="big")]


    def __str__(self): return f"value: {self.value}"
