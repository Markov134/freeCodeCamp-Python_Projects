class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        if not isinstance(key, str):
            return 'key must be a string'
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value
    
    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                del self.collection[hash_value][key]
        return

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            if key in self.collection[hash_value]:
                return self.collection[hash_value][key]
        return None


