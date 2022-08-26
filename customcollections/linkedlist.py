class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __del__(self):
        self.data = None
        self.next = None


class LinkedList:
    __root = None
    __last = None
    __current = None
    __index = None
    __counter = None

    @staticmethod
    def comparer(o1, o2):
        return o1 == o2

    def __init__(self):
        self.__root = None
        self.__last = None
        self.__counter = 0
        self.__index = 0
        self.__current = self.__root

    def __len__(self):
        return self.len()

    def __iter__(self):
        self.reset()
        return self

    def __next__(self):
        # fixme: endless iteration
        return self.next()

    def __contains__(self, item):
        result, i = self.find(item)
        return not result == None

    def __setitem__(self, index, value):
        self.reset()
        i = -1
        while 1:
            if i < index-1:
                o, i = self.next()
            else:
                self.__current.data = value
                return

    def __getitem__(self, index):
        self.reset()
        i = 0
        for o, i in iter(self):
            print(o, i)

    def reset(self):
        self.__current = self.__root
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
            return None, None
        return result, index

    def append(self, value=None):
        node = Node(value)
        if not self.__root:
            self.__last = node
            self.__root = node
            self.__current = self.__root
        else:
            self.__last.next = node
            self.__last = node
        self.__counter += 1
        return self

    def clear(self):
        current = self.__root
        if current:
            while 1:
                if current.next:
                    tmp = current.next
                    current.__del__()
                    current = tmp
                else:
                    current.__del__()
                    self.__root = None
                    self.__last = None
                    self.__counter = 0
                    return True

    def remove(self, value, comparer=None):
        prev = None
        current = self.__root
        local_counter = 0

        if comparer:
            is_equal = comparer
        else:
            is_equal = self.comparer

        while 1:
            if is_equal(current.data, value):
                result = current.data
                # try to remove the __root node
                if not prev:
                    self.__init__()
                    return result

                # try to remove the __last node
                if not current.next:
                    prev.next = None
                    self.__last = prev
                    current.__del__()
                else:
                    prev.next = current.next
                    current.__del__()
                self.__counter -= 1
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
        current = self.__root

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
        current = self.__root
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
            node = self.__root
        print(node.data)
        if node.next:
            self.print(node.next)
        return None

    def to_array(self):
        result = [None] * self.__counter
        local_counter = 0
        current = self.__root
        if self.__counter < 1:
            return []
        while 1:
            result[local_counter] = current.data
            if current.next:
                current = current.next
                local_counter += 1
            else:
                return result
        return []

    def len(self):
        return self.__counter

    def get_last(self):
        return self.__last

    def get_root(self):
        return self.__root

    def serialize(self):
        # todo: serialize
        pass