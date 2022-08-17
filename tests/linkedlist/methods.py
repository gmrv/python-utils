import unittest
from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append(self):
        result = LinkedList().append(0).append(1).append(2).to_array()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 2)

    def test_clear(self):
        source = LinkedList().append(1).append(2).append(3).append(4).append(5).append(2)
        source.clear()
        result = source.to_array()
        self.assertEqual(result, [])

    def test_find(self):
        comparer = lambda o1, o2: o1["id"] == o2["id"] and o1["val"] == o2["val"]
        source = LinkedList().append({"id": 1, "val": "str1"}).append({"id": 2, "val": "str2"}).append(
            {"id": 3, "val": "str3"})
        obj, index = source.find({"id": 2, "val": "str2"}, comparer=comparer)
        if obj:
            self.assertEqual(obj["id"], 2)
            self.assertEqual(index, 1)
        obj, index = source.find({"id": 2, "val": "sss"}, comparer=comparer)
        self.assertEqual(obj, None)

    def test_find_all(self):
        source = LinkedList().append(1).append(2).append(3).append(4).append(5).append(2)
        result = source.find_all(2)
        self.assertEqual(len(result), 2)
        result = source.find_all(9)
        self.assertEqual(len(result), 0)

    def test_remove(self):
        source = LinkedList().append(1).append(2).append(3).append(4).append(5).append(2)
        removed = source.remove(2)
        removed = source.remove(2)
        result = source.to_array()
        self.assertEqual(removed, 2)
        self.assertEqual(len(result), 4)

    def test_reset(self):
        lst = LinkedList().append(0).append(1).append(2)

        data, index = lst.next()
        self.assertEqual(data, 0)
        self.assertEqual(index, 0)

        data, index = lst.next()
        self.assertEqual(data, 1)
        self.assertEqual(index, 1)

        data, index = lst.next(reset=True)
        self.assertEqual(data, 0)
        self.assertEqual(index, 0)

    def test_to_array(self):
        source = LinkedList().append(1).append(2).append(3)
        result = source.to_array()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 2)
        self.assertEqual(result[2], 3)
        self.assertEqual(len(result), 3)


if __name__ == '__main__':
    unittest.main()
