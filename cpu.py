from stack import Stack
from opcodes import *
from arithmetic import *
from push import *


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
            # ARITHMETIC
            if op == ADD:    add(cpu)
            if op == MUL:    mul(cpu)
            if op == SUB:    sub(cpu)
            if op == DIV:    div(cpu)
            if op == SDIV:   sdiv(cpu)
            if op == MOD:    mod(cpu)
            if op == SMOD:   smod(cpu)
            if op == ADDMOD: addmod(cpu)
            if op == EXP:    exp(cpu)

            # PUSH
            if op == PUSH1:
                self.push(1)
                self.pc += 1
            if op == PUSH2:
                self.push(2)
                self.pc += 2
            if op == PUSH3:
                self.push(3)
                self.pc += 3
            if op == PUSH4:
                self.push(4)
                self.pc += 4
            if op == PUSH5:
                self.push(5)
                self.pc += 5
            if op == PUSH6:
                self.push(6)
                self.pc += 6
            if op == PUSH7:
                self.push(7)
                self.pc += 7
            if op == PUSH8:
                self.push(8)
                self.pc += 8
            if op == PUSH9:
                self.push(9)
                self.pc += 9
            if op == PUSH10:
                self.push(10)
                self.pc += 10
            if op == PUSH11:
                self.push(11)
                self.pc += 11
            if op == PUSH12:
                self.push(12)
                self.pc += 12
            if op == PUSH13:
                self.push(13)
                self.pc += 13
            if op == PUSH14:
                self.push(14)
                self.pc += 14
            if op == PUSH15:
                self.push(15)
                self.pc += 15
            if op == PUSH16:
                self.push(16)
                self.pc += 16
            if op == PUSH17:
                self.push(17)
                self.pc += 17
            if op == PUSH18:
                self.push(18)
                self.pc += 18
            if op == PUSH19:
                self.push(19)
                self.pc += 19
            if op == PUSH20:
                self.push(20)
                self.pc += 20
            if op == PUSH21:
                self.push(21)
                self.pc += 21
            if op == PUSH22:
                self.push(22)
                self.pc += 22
            if op == PUSH23:
                self.push(23)
            if op == PUSH24:
                self.push(24)
                self.pc += 24
            if op == PUSH25:
                self.push(25)
                self.pc += 25
            if op == PUSH26:
                self.push(26)
                self.pc += 26
            if op == PUSH27:
                self.push(27)
                self.pc += 27
            if op == PUSH28:
                self.push(28)
                self.pc += 28
            if op == PUSH29:
                self.push(29)
                self.pc += 29
            if op == PUSH30:
                self.push(30)
                self.pc += 30
            if op == PUSH31:
                self.push(31)
                self.pc += 31
            if op == PUSH32:
                self.push(32)
                self.pc += 32
