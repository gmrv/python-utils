import customcollections


class HashTable:
    storage = None
    def __init__(self, init_size=10):
        self.storage = [None] * init_size

    def get_hash(self, value):
        result = 0
        value_str = str(value)
        index_size = len(self.storage)
        for ch in value_str:
            result = ((index_size-1) * result + ord(ch)) % index_size
            result = (result * 2 + 1) % index_size
        return result

    def add(self, value):
        ll = customcollections.LinkedList()
        index = self.get_hash(value)
        if self.storage[index]:
            ll = self.storage[index]
            ll.append(value)
        else:
            self.storage[index] = ll.append(value)

    def has(self, value):
        index = self.get_hash(value)
        if self.storage[index]:
            ll = self.storage[index]
            data, ind = ll.find(value)
            if data:
                return True
            else:
                return False
        else:
            return False