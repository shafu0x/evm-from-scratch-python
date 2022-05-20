class Storage:
    def __init__(self):
        self.storage = {}
        self.cache = []

    def store(self, key, value):
        old_value = self.load(key)
        self.storage[key] = value

        warm = True if key in self.cache else False
        return warm, old_value

    def load(self, key):
        warm = True if key in self.cache else False

        # every key-value pair exists
        if key not in self.storage: return 0x00


        return warm, self.storage[key]
