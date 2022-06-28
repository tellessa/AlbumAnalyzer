# import algorithms.my_algorithms
import sys
import unittest
print(sys.path)


# print(binary_search(my_list, 3))  # => 1
# print(binary_search(my_list, -1))  # => None


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_3():
        my_list = [1, 3, 5, 7, 9]
        assert binary_search(my_list, 3) == 1

    def test_binary_search_neg():
        my_list = [1, 3, 5, 7, 9]
        assert binary_search(my_list, -1) is None
