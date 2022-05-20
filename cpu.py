from stack import Stack
from opcodes import *
from arithmetic import *
from push import _push
from comp import *
from logic import *
from bit import *
from env import *
from memory import *
from storage import *
from memory_ops import *
from misc import *
from account import *
from storage import *
from jump import *
from dup import *
from swap import *


# TODO: rename to execution engine or something
class CPU:
    def __init__(self, 
                 program,
                 balance,
                 available_gas,
                 calldata=[],
                 prev_returndata=[]):
        self.pc = 0
        self.balance = balance
        self.stack = Stack()
        self.memory = Memory()
        self.storage = Storage()
        self.program = self.load(program)

        self.stop_flag = False

        # inputs to program
        self.gas = available_gas # TODO
        self.calldata = calldata

        # return of prev call
        self.prev_returndata = prev_returndata

        # cache
        self.address_cache = []

        # output 
        self.returndata = []
        self.logs = []

    def load(self, program):
        self.reset()
        return program

    def append_log(log): self.logs.append(log)

    def reset(self):
        self.pc, self.stack = 0, Stack()
        self.memory, self.storage =  Memory(), Storage()

    def peek(self):
        return self.program[self.pc]

    def gas_dec(self, amount):
        if self.gas - amount < 0: 
            raise Exception(f"{self.gas} gas left and {amount} required")
        self.gas -= amount

    def access_account(self, address):
        warm = False # check if address is warm or cold

        if address in self.address_cache: warm = True
        else                            : self.address_cache.append(address)

        return warm, Account([0xFF], 0xAA)

    def gas_inc(self, amount):
        self.gas += amount

    # check if we want to run the next opcode
    def exec_next_opcode(self):
        if self.pc > len(self.program)-1      : return False
        if self.stop_flag                     : return False
        if not is_valid(self.program[self.pc]): return False

        return True

    def run(self):
        # run until we run out of opcodes
        while self.exec_next_opcode():
            op = self.program[self.pc]
            print("op: ", hex(op))
            print("pc: " , self.pc)

            # ARITHMETIC
            if op == ADD:        add(self)
            if op == MUL:        mul(self)
            if op == SUB:        sub(self)
            if op == DIV:        div(self)
            if op == SDIV:       sdiv(self)
            if op == MOD:        mod(self)
            if op == SMOD:       smod(self)
            if op == ADDMOD:     addmod(self)
            if op == MULMOD:     mulmod(self)
            if op == ADDMOD:     addmod(self)
            if op == EXP:        exp(self)
            if op == SIGNEXTEND: signextend(self)

            # COMP
            if op == LT:     lt(self)
            if op == GT:     gt(self)
            if op == EQ:     eq(self)
            if op == ISZERO: iszero(self)

            # LOGIC
            if op == AND: _and(self)
            if op == OR:  _or(self)
            if op == XOR: _xor(self)
            if op == NOT: _not(self)

            # BIT
            if op == SHL: shl(self)
            if op == SHR: shr(self)

            # MISC
            if op == SHA3:         sha3(self)
            if op == SELFDESTRUCT: selfdestruct(self)
            if op == RETURN:       _return(self)

            # ENV
            if op == ADDRESS:      address(self)
            if op == BALANCE:      balance(self)
            if op == ORIGIN:       origin(self)
            if op == CALLER:       caller(self)
            if op == CALLVALUE:    callvalue(self)
            if op == CALLDATALOAD: calldataload(self)
            if op == CALLDATASIZE: calldatasize(self)
            if op == CALLDATACOPY: calldatacopy(self)
            if op == CODESIZE:     codesize(self)
            if op == CODECOPY:     codecopy(self)
            if op == GASPRICE:     gasprice(self)

            # MEMORY
            if op == BYTE:    byte(self)
            if op == MLOAD:   mload(self)
            if op == MSTORE8: mstore8(self)
            if op == MSTORE:  mstore(self)

            # MEMORY
            if op == SLOAD:    sload(self)
            if op == SSTORE:   sstore(self)

            # JUMP
            if op == JUMP:      jump(self)
            if op == JUMPI:     jumpi(self)
            if op == PC:        pc(self)
            if op == JUMPDEST:  jumpest(self)

            # PUSH
            if op == PUSH1:   _push(self, 1)
            if op == PUSH2:   _push(self, 2)
            if op == PUSH3:   _push(self, 3)
            if op == PUSH4:   _push(self, 4)
            if op == PUSH5:   _push(self, 5)
            if op == PUSH6:   _push(self, 6)
            if op == PUSH7:   _push(self, 7)
            if op == PUSH8:   _push(self, 8)
            if op == PUSH9:   _push(self, 9)
            if op == PUSH10:  _push(self, 10)
            if op == PUSH11:  _push(self, 11)
            if op == PUSH12:  _push(self, 12)
            if op == PUSH13:  _push(self, 13)
            if op == PUSH14:  _push(self, 14)
            if op == PUSH15:  _push(self, 15)
            if op == PUSH16:  _push(self, 16)
            if op == PUSH17:  _push(self, 17)
            if op == PUSH18:  _push(self, 18)
            if op == PUSH19:  _push(self, 19)
            if op == PUSH20:  _push(self, 20)
            if op == PUSH21:  _push(self, 21)
            if op == PUSH22:  _push(self, 22)
            if op == PUSH23:  _push(self, 23)
            if op == PUSH24:  _push(self, 24)
            if op == PUSH25:  _push(self, 25)
            if op == PUSH26:  _push(self, 26)
            if op == PUSH27:  _push(self, 27)
            if op == PUSH28:  _push(self, 28)
            if op == PUSH29:  _push(self, 29)
            if op == PUSH30:  _push(self, 30)
            if op == PUSH31:  _push(self, 31)
            if op == PUSH32:  _push(self, 32)

            # DUP
            if op == DUP1:   _dup(self, 1)
            if op == DUP2:   _dup(self, 2)
            if op == DUP3:   _dup(self, 3)
            if op == DUP4:   _dup(self, 4)
            if op == DUP5:   _dup(self, 5)
            if op == DUP6:   _dup(self, 6)
            if op == DUP7:   _dup(self, 7)
            if op == DUP8:   _dup(self, 8)
            if op == DUP9:   _dup(self, 9)
            if op == DUP10:  _dup(self, 10)
            if op == DUP11:  _dup(self, 11)
            if op == DUP12:  _dup(self, 12)
            if op == DUP13:  _dup(self, 13)
            if op == DUP14:  _dup(self, 14)
            if op == DUP15:  _dup(self, 15)
            if op == DUP16:  _dup(self, 16)

            # SWAP
            if op == SWAP1:   _swap(self, 1)
            if op == SWAP2:   _swap(self, 2)
            if op == SWAP3:   _swap(self, 3)
            if op == SWAP4:   _swap(self, 4)
            if op == SWAP5:   _swap(self, 5)
            if op == SWAP6:   _swap(self, 6)
            if op == SWAP7:   _swap(self, 7)
            if op == SWAP8:   _swap(self, 8)
            if op == SWAP9:   _swap(self, 9)
            if op == SWAP10:  _swap(self, 10)
            if op == SWAP11:  _swap(self, 11)
            if op == SWAP12:  _swap(self, 12)
            if op == SWAP13:  _swap(self, 13)
            if op == SWAP14:  _swap(self, 14)
            if op == SWAP15:  _swap(self, 15)
            if op == SWAP16:  _swap(self, 16)

            print("gas: ", self.gas)
            print("stack: ", self.stack)
            print("memory: ", self.memory.memory)

        # TODO: return things
