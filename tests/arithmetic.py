import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
from computer.cpu import *
from ethereum.number import *

PUSH = [0x60, 0x03, 0x60, 0x02]

class TestArithmetic(unittest.TestCase):

    def test_add(self):
        PROGRAM = PUSH + [0x01]
        cpu = CPU(PROGRAM, 0, 21000, [], [])
        cpu.run()

        self.assertEqual(cpu.stack.get(0).value, 0x05)

    def test_add(self):
        PROGRAM = PUSH + [0x02]
        cpu = CPU(PROGRAM, 0, 21000, [], [])
        cpu.run()

        self.assertEqual(cpu.stack.get(0).value, 0x06)

    def test_sub(self):
        PROGRAM = PUSH + [0x03]
        cpu = CPU(PROGRAM, 0, 21000, [], [])
        cpu.run()

        self.assertEqual(cpu.stack.get(0).value, MAX_UINT-1)

if __name__ == '__main__':
    unittest.main()
