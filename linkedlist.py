class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    root = None
    current = None
    counter = None

    def __init__(self):
        self.root = None
        self.current = None
        self.counter = 0

    def append(self, value=None):
        node = Node(value)
        if not self.root:
            self.current = node
            self.root = node
        else:
            self.current.next = node
            self.current = node
        self.counter += 1
        return self

    def remove(self, value, comparer=None):
        local_counter = 0
        local_current = self.root
        prev = None
        delete_this = False
        while 1:
            if comparer:
                delete_this = comparer(local_current.data, value)
            else:
                delete_this = (local_current.data == value)

            if delete_this:

                # try to remove the root node
                if not prev:
                    raise Exception("Can't remove the root node")

                # try to remove the last node
                if not local_current.next:
                    prev.next = None
                else:
                    prev.next = local_current.next
                self.counter -= 1
                return 0

            if local_current.next:
                prev = local_current
                local_current = local_current.next
                local_counter += 1
            else:
                return 0

        raise Exception("Something went wrong")

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
        local_current = self.root
        while 1:
            result[local_counter] = local_current.data
            if local_current.next:
                local_current = local_current.next
                local_counter += 1
            else:
                return result
        return -1


list1 = LinkedList().append(1).append(2).append(3).append(4).append(5)
list1.remove(4)
list1.remove(3)
list1.remove(2)

ll = LinkedList()

obj1 = {
    "id": 1,
    "data": "str",
}

obj2 = {
    "id": 2,
    "data": "str",
}

obj3 = {
    "id": 3,
    "data": "str",
}

obj4 = {
    "id": 2,
    "data": "str2",
}

ll.append(obj1).append(obj2).append(obj3)
ll.remove(obj4, (lambda o1, o2 : o1["id"] == o2["id"]))

print(list1.to_array())
print(ll.to_array())