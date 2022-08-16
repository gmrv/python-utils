import unittest
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):

    list = LinkedList().append(0).append(1).append(2)

    def test_append(self):
        result = LinkedList().append(0).append(1).append(2).to_array()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 2)

    def test_reset(self):
        data, index = self.list.next()
        self.assertEqual(data, 0)
        self.assertEqual(index, 0)

        data, index = self.list.next()
        self.assertEqual(data, 1)
        self.assertEqual(index, 1)

        data, index = self.list.next(reset=True)
        self.assertEqual(data, 0)
        self.assertEqual(index, 0)



if __name__ == '__main__':
    unittest.main()
