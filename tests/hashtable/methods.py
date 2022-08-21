import random
import string
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

    def test_get(self):
        ht = HashTable(init_size=10)
        ht.add('Me value', "3data-data-data")
        ht.add('horse', "4data-data-data")
        ht.add(111, "5data-data-data")
        ht.add(1234567890, "6data-data-data")
        self.assertEqual(ht.get('horse'), "4data-data-data")
        self.assertEqual(ht.get('Me value'), "3data-data-data")
        self.assertEqual(ht.get(1234567890), "6data-data-data")

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
