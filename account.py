from eth_hash.auto import keccak

class Account:
    def __init__(self, code, balance):
        self.code = code
        self.balance = balance
        self.codesize = len(code)
        self.hash = keccak(code)
