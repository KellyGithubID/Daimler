import unittest
from Codes.BinarySearch import *


class BinarySearchTest(unittest.TestCase):
    def test_empty_array(self):
        empty_array = []
        target_number = 1
        test_search = BinarySearch(empty_array, target_number)
        self.assertEqual(-1, test_search.search_index_of_target_number())

    def test_one_number_array_with_target_number(self):
        one_number_array = [1]
        target_number = 1
        test_search = BinarySearch(one_number_array, target_number)
        self.assertEqual(0, test_search.search_index_of_target_number())

    def test_one_number_array_without_target_number(self):
        one_number_array = [1]
        target_number = 3
        test_search = BinarySearch(one_number_array, target_number)
        self.assertEqual(-1, test_search.search_index_of_target_number())

    def test_two_numbers_array_with_lower_target_number(self):
        two_numbers_array = [1, 3]
        lower_target_number = 1
        test_search = BinarySearch(two_numbers_array, lower_target_number)
        self.assertEqual(0, test_search.search_index_of_target_number())

    def test_two_numbers_array_with_higher_target_number(self):
        two_numbers_array = [1, 3]
        higher_target_number = 3
        test_search = BinarySearch(two_numbers_array, higher_target_number)
        self.assertEqual(1, test_search.search_index_of_target_number())

    def test_two_numbers_array_without_target_number(self):
        two_numbers_array = [1, 3]
        target_number = 2
        test_search = BinarySearch(two_numbers_array, target_number)
        self.assertEqual(-1, test_search.search_index_of_target_number())

    def test_even_numbers_array_with_target_number(self):
        even_numbers_array = [1, 3, 5, 7]
        target_number = 5
        test_search = BinarySearch(even_numbers_array, target_number)
        self.assertEqual(2, test_search.search_index_of_target_number())

    def test_even_numbers_array_without_target_number(self):
        even_numbers_array = [1, 3, 5, 7]
        target_number = 9
        test_search = BinarySearch(even_numbers_array, target_number)
        self.assertEqual(-1, test_search.search_index_of_target_number())

    def test_odd_numbers_array_with_target_number(self):
        odd_numbers_array = [1, 3, 5, 7, 9]
        target_number = 7
        test_search = BinarySearch(odd_numbers_array, target_number)
        self.assertEqual(3, test_search.search_index_of_target_number())

    def test_odd_numbers_array_without_target_number(self):
        odd_numbers_array = [1, 3, 5, 7, 9]
        target_number = 0
        test_search = BinarySearch(odd_numbers_array, target_number)
        self.assertEqual(-1, test_search.search_index_of_target_number())

        

if __name__ == '__main__':
    unittest.main()
