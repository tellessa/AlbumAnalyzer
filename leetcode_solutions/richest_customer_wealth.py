from typing import List
import unittest


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealths = []
        for array in accounts:
            wealth = 0
            for number in array:
                wealth += number
            wealths.append(wealth)

        return max(wealths)


"""
m x n integer grid

m is the number of inner arrays, or columns
n is the number of items per inner array, or rows

accounts[i][j]
i is the customer index
j is the bank index
wealth is the amount of money thye have in all their bank accounts
max wealth means richest customer
"""


class TestSolution(unittest.TestCase):
    def test_richest_customer_123_321(self, accounts: List[List[int]]) -> int:
        solution = Solution()
        assert 6 == solution.maximumWealth([[1, 2, 3], [3, 2, 1]])

    def test_richest_customer_15_73_35(self, accounts: List[List[int]]) -> int:
        solution = Solution()
        assert 10 == solution.maximumWealth([[1, 5], [7, 3], [3, 5]])

    def test_richest_customer_287_713_195(self, accounts: List[List[int]]) -> int:
        solution = Solution()
        assert 17 == solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumWealth([[1, 2, 3], [3, 2, 1]]))
    print(solution.maximumWealth([[1, 5], [7, 3], [3, 5]]))
    print(solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
