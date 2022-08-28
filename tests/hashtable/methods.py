import random
import string
import unittest
from customcollections import *


class TestHashTable(unittest.TestCase):

    def test_attributes(self):
        ht1 = HashTable(init_size=10)
        ht1["mykey"] = 1
        ht1["myotherkey"] = 2
        self.assertEqual(ht1["mykey"], 1)
        self.assertEqual(ht1["myotherkey"], 2)

    def test_add_and_has(self):
        ht = HashTable(init_size=10)

        # Test for adding empty data
        with self.assertRaises(HashTableExceptionKeyValueItemRequired):
            ht.add()

        # Test for adding data as HashTableItem object
        ri = ht.add(item=HashTableItem('item-key', 'item-value'))
        self.assertEqual(ri.key, 'item-key')

        # Test for adding duplicate key
        r1 = ht.add('Me value', "1data-data-data")
        with self.assertRaises(HashTableExceptionDuplicateKey):
            r2 = ht.add('Me value', "2data-data-data")

        ht.add('horse', "4data-data-data")
        ht.add(111, "5data-data-data")
        ht.add(1234567890, "6data-data-data")

        self.assertEqual(True, ht.has('Me value'))
        self.assertEqual(True, ht.has(111))
        self.assertEqual(False, ht.has('Very long sentence'))
        self.assertEqual(True, ht.has(1234567890))

    def test_get(self):
        ht = HashTable(init_size=10)
        ht.add('Me value', "3data-data-data")
        ht.add('horse', "4data-data-data")
        ht.add(111, "5data-data-data")
        ht.add(1234567890, "6data-data-data")
        self.assertEqual(ht.get('horse'), "4data-data-data")
        self.assertEqual(ht.get('Me value'), "3data-data-data")
        self.assertEqual(ht.get(1234567890), "6data-data-data")

    def test_remove(self):
        ht = HashTable(init_size=5)
        ht.add(111, "1data-data-data")
        ht.add(222, "2data-data-data")
        ht.add(333, "3data-data-data")
        ht.add(444, "4data-data-data")
        ht.add(555, "5data-data-data")
        ht.add(666, "6data-data-data")
        ht.add(777, "7data-data-data")
        ht.add(888, "8data-data-data")
        ht.remove(555)
        ht.remove(666)
        ht.remove(111)
        ht.add(555, "5data-data-data")
        ht.add(666, "6data-data-data")
        ht.add(111, "1data-111-data")
        self.assertEqual(ht.get(111), "1data-111-data")

    def test_fullness(self):
        letters = string.ascii_lowercase
        ht = HashTable(init_size=100)
        for i in range(1, 100):
            key = ''.join(random.choice(letters) for i in range(10))
            # print(i, key)
            ht.add(key, "data-data-data")

        fullness = ht.show_fullness() * 100
        self.assertGreater(fullness, 50)

        pass
