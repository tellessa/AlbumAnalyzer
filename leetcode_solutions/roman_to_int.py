import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        pass


class TestSolution(unittest.TestCase):
    def test_romanToInt_3(self, s: str) -> int:
        solution = Solution()
        assert 3 == solution.romanToInt("III")

    def test_romanToInt_58(self, s: str) -> int:
        solution = Solution()
        assert 3 == solution.romanToInt("III")

    def test_romanToInt_1994(self, s: str) -> int:
        solution = Solution()
        assert 3 == solution.romanToInt("III")
