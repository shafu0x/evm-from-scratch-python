# TODO: check for overflow
def add(stack):
    a = stack.pop()
    b = stack.pop()
    stack.push(a + b)
