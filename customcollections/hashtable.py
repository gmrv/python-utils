import customcollections
import hashlib


class HashTableItem:
    key = None
    data = None

    def __init__(self, key=key, data=data):
        self.key = key
        self.data = data


class HashTable:
    storage = None

    def __init__(self, init_size=10):
        self.storage = [None] * init_size

    @staticmethod
    def comparer(self, o1, o2):
        result = o1.key == o2.key
        return result

    def get_hash(self, key):
        # todo: testing hashes
        return self.get_hashlib_hash(str(key))

    def get_custom_hash(self, key):
        result = 0
        value_str = str(key)
        storage_size = len(self.storage)
        for ch in value_str:
            result = ((storage_size - 0) * result + ord(ch)) % storage_size
            # result = (result * 3.14 + 0) % storage_size
            result = (result * 2 + 0) % storage_size
        return result

    def get_hash_hash(self, key):
        result = abs(hash(key)) % len(self.storage)
        return result

    def get_hashlib_hash(self, key):
        result = int(hashlib.sha1(key.encode("utf-8")).hexdigest(), 16) % len(self.storage)
        return result

    def add(self, key, value):
        ll = customcollections.LinkedList()
        index = self.get_hash(key)
        if self.storage[index]:
            ll = self.storage[index]
            ll.append(HashTableItem(key=key, data=value))
        else:
            self.storage[index] = ll.append(HashTableItem(key=key, data=value))

    def has(self, key):
        index = self.get_hash(key)
        if self.storage[index]:
            ll = self.storage[index]
            data, ind = ll.find(HashTableItem(key=key, data=None), comparer=self.comparer)
            if data:
                return True
            else:
                return False
        else:
            return False

    def show_fullness(self):
        counter = 0
        for i in range(0, len(self.storage) - 1):
            if self.storage[i]:
                counter += 1
        return counter / len(self.storage)
