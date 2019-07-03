import unittest
from Codes.BinarySearch import *


class BinarySearchTest(unittest.TestCase):
    def test_empty_array(self):
        empty_array = []
        target_number = 1
        test_search = BinarySearch(empty_array, target_number)
        self.assertEqual(-1, test_search.search_index_of_target_number())


if __name__ == '__main__':
    unittest.main()
