class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __del__(self):
        self.data = None
        self.next = None


class LinkedList:
    root = None
    last = None
    __current = None
    __index = None
    counter = None
    comparer = lambda self, o1, o2: o1 == o2

    def __init__(self):
        self.root = None
        self.last = None
        self.counter = 0
        self.__index = 0
        self.__current = self.root

    def reset(self):
        self.__current = self.root
        self.__index = 0
        return self.__index

    def next(self, reset=False):
        if reset:
            self.reset()
        if not self.__current:
            return None, None
        result = self.__current.data
        index = self.__index
        if self.__current.next:
            self.__current = self.__current.next
            self.__index += 1
        else:
            self.__current = None
            return result, index
        return result, index

    def append(self, value=None):
        node = Node(value)
        if not self.root:
            self.last = node
            self.root = node
            self.__current = self.root
        else:
            self.last.next = node
            self.last = node
        self.counter += 1
        return self

    def clear(self):
        current = self.root
        if current:
            while 1:
                if current.next:
                    tmp = current.next
                    current.__del__()
                    current = tmp
                else:
                    current.__del__()
                    self.root = None
                    self.last = None
                    self.counter = 0
                    return True

    def remove(self, value, comparer=None):
        prev = None
        current = self.root
        local_counter = 0

        if comparer:
            is_equal = comparer
        else:
            is_equal = self.comparer

        while 1:
            if is_equal(current.data, value):
                result = current.data
                # try to remove the root node
                if not prev:
                    raise Exception("Can't remove the root node")

                # try to remove the last node
                if not current.next:
                    prev.next = None
                    self.last = prev
                    current.__del__()
                else:
                    prev.next = current.next
                    current.__del__()
                self.counter -= 1
                return result

            if current.next:
                prev = current
                current = current.next
                local_counter += 1
            else:
                # reach the end
                return None
        return None

    def find(self, value, comparer=None):
        local_counter = 0
        current = self.root

        if comparer:
            is_equal = comparer
        else:
            is_equal = self.comparer

        while 1:
            if is_equal(current.data, value):
                return current.data, local_counter
            else:
                if current.next:
                    current = current.next
                    local_counter += 1
                else:
                    return None, None
        return None, None

    def find_all(self, value, comparer=None):
        local_counter = 0
        current = self.root
        result = []

        if comparer:
            is_equal = comparer
        else:
            is_equal = self.comparer

        while 1:
            if is_equal(current.data, value):
                result.append(current.data)

            if current.next:
                current = current.next
                local_counter += 1
            else:
                return result
        return result

    def print(self, node=None):
        if not node:
            node = self.root
        print(node.data)
        if node.next:
            self.print(node.next)
        return None

    def to_array(self):
        result = [None] * self.counter
        local_counter = 0
        current = self.root
        if self.counter < 1:
            return []
        while 1:
            result[local_counter] = current.data
            if current.next:
                current = current.next
                local_counter += 1
            else:
                return result
        return []

    def serialize(self):
        # todo: serialize
        pass