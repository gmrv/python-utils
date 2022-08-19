import unittest
from customcollections import HashTable


class TestHashTable(unittest.TestCase):

    def test_add_and_has(self):
        ht = HashTable(init_size=10)

        ht.add('Me value', "1data-data-data")
        ht.add('Me value', "2data-data-data")
        ht.add('Me value', "3data-data-data")

        ht.add('horse', "4data-data-data")
        ht.add(111, "5data-data-data")
        ht.add(1234567890, "6data-data-data")

        self.assertEqual(True, ht.has('Me value'))
        self.assertEqual(True, ht.has(111))
        self.assertEqual(False, ht.has('Very long sentence'))
        self.assertEqual(True, ht.has(1234567890))

    def test_hash(self):
        ht = HashTable(init_size=10)
        self.assertEqual(9, ht.get_hash('test'))
        self.assertEqual(7, ht.get_hash('horse'))
        self.assertEqual(5, ht.get_hash('Very long sentence'))
        self.assertEqual(5, ht.get_hash(1234567890))
        self.assertEqual(9, ht.get_hash(1))
        self.assertEqual(7, ht.get_hash(111))
