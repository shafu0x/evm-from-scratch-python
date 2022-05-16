class StackTooLargeException(Exception):
    pass
class StackEmptyException(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0: raise StackEmptyException()

        return self.stack.pop()

    def push(self, data):
        if len(self.stack) > 1024: raise StackTooLargeException()

        self.stack.append(data)
