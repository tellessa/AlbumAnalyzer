import unittest
from my_algorithms import grokking_alg_binary_search
import sys
sys.path.append('c:\\Users\\StephenTelles\\repo\\data_engineering\\algorithms')
print(sys.path)


# def grokking_alg_binary_search(list, item):
#     low = 0
#     high = len(list) - 1

#     while low <= high:
#         mid = (low + high) // 2  # The book had division, adjusted to floor division
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None


# def ask_python_com_binary_search(list, target):
#     low = 0
#     high = len(list) - 1

#     while(low <= high):
#         mid = (low + high) // 2
#         if(list[mid] > target):
#             high = mid - 1
#         elif(list[mid] < target):
#             low = mid + 1
#         else:
#             return mid
#     return None


# print(binary_search(my_list, 3))  # => 1
# print(binary_search(my_list, -1))  # => None


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_3(self):
        my_list = [1, 3, 5, 7, 9]
        # assert algorithms.my_algorithms.binary_search(my_list, 3) == 1
        assert grokking_alg_binary_search(my_list, 3) == 1

    def test_binary_search_neg(self):
        my_list = [1, 3, 5, 7, 9]
        # assert algorithms.my_algorithms.binary_search(my_list, -1) is None
        assert grokking_alg_binary_search(my_list, -1) is None
