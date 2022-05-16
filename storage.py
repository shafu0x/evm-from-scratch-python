class Storage:
    def __init__(self):
        self.storage = {}

    def store(self, key, value):
        self.storage[key] = value

    def load(self, key):
        return self.storage[key]
