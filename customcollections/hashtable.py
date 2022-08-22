import hashlib
from customcollections import LinkedList


class HashTableItem:
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTableExceptionKeyValueItemRequired(Exception):

    message = 'Key, value or HashTableItem object required'

    def __init__(self):
        super().__init__(self.message)


class HashTable:
    storage: [LinkedList] = None

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
            result = (result * 2 + 0) % storage_size
        return result

    def get_hash_hash(self, key):
        result = abs(hash(key)) % len(self.storage)
        return result

    def get_hashlib_hash(self, key):
        result = int(hashlib.sha1(key.encode("utf-8")).hexdigest(), 16) % len(self.storage)
        return result

    def add(self, key=None, value=None, item: HashTableItem = None):

        if not((key and value) or item):
            raise HashTableExceptionKeyValueItemRequired()

        if item:
            key = item.key
            value = item.value

        if self.has(key):
            return None
        ll = LinkedList()
        index = self.get_hash(key)
        if self.storage[index]:
            ll: LinkedList = self.storage[index]
            o = HashTableItem(key=key, value=value)
            ll.append(o)
            return o
        else:
            o = HashTableItem(key=key, value=value)
            self.storage[index] = ll.append(o)
            return o

    def has(self, key):
        index = self.get_hash(key)
        if self.storage[index]:
            ll: LinkedList = self.storage[index]
            data, ind = ll.find(HashTableItem(key=key, value=None), comparer=self.comparer)
            if data:
                return True
            else:
                return False
        else:
            return False

    def get(self, key):
        index = self.get_hash(key)
        if self.storage[index]:
            ll: LinkedList = self.storage[index]
            data, ind = ll.find(HashTableItem(key=key, value=None), comparer=self.comparer)
            if data:
                return data.value
            else:
                return None
        else:
            return None

    def remove(self, key):
        index = self.get_hash(key)
        if self.storage[index]:
            ll: LinkedList = self.storage[index]
            ll.remove(HashTableItem(key=key, value=None), comparer=self.comparer)
            if ll.counter == 0:
                self.storage[index] = None

    def show_fullness(self):
        counter = 0
        for i in range(0, len(self.storage) - 1):
            if self.storage[i]:
                counter += 1
        return counter / len(self.storage)
