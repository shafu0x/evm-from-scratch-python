from stack import Stack
from opcodes import *
from ops import *


class CPU:
    def __init__(self):
        self.pc = 0
        self.stack = Stack()
        self.program = []

    def load(self, program):
        self.reset()
        self.program = program

    def reset(self):
        self.pc, self.stack = 0, []

    def peek(self, i=1):
        return self.program[self.pc + i]

    def run(self):
        op = self.program[self.pc]

        while op != STOP:
            if op == ADD:
                add()
                self.pc += 1
            break
