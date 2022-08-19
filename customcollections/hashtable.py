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

    def add(self, key, value):
        ll = customcollections.LinkedList()
        index = self.get_hash(key)
        if self.storage[index]:
            ll = self.storage[index]
            # todo: dict {"key": key, "value": value} to object
            ll.append({"key": key, "value": value})
        else:
            self.storage[index] = ll.append({"key": key, "value": value})

    def has(self, key):
        index = self.get_hash(key)
        if self.storage[index]:
            ll = self.storage[index]
            data, ind = ll.find({"key": key, "value": None}, comparer=self.comparer)
            if data:
                return True
            else:
                return False
        else:
            return False

    def comparer(self, o1, o2):
        result = o1["key"] == o2["key"]
        return result