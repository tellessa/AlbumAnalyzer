import unittest

# There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#     Given a roman numeral, convert it to an integer.

# constraints
# --> come back to these constraints to narrow the general answer
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# --> We don't have to handle absurd cases
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
# --> 3999 in roman numerals:

# Roman numerals are usually written largest to smallest from left to right.
#     However, the numeral for four is not IIII.
#     Instead, the number four is written as IV.
#     Because the one is before the five we subtract it making four.
#     The same principle applies to the number nine, which is written as IX.


# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def romanToInt(self, s: str) -> int:

        # Set up the basic mapping
        symbols_to_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # convert to list since strings are immutable
        list_of_letters = [letter for letter in s]
        arabic_number = 0
        while len(list_of_letters):
            letter = list_of_letters.pop()
            if len(list_of_letters):
                # Get the letter before the letter
                letter_before = list_of_letters[-1]
                # If the letter needs to be subtracted
                if symbols_to_values[letter] > symbols_to_values[letter_before]:
                    # Pop the letter before so we don't sum it
                    letter_before = list_of_letters.pop()
                    value = symbols_to_values[letter] - symbols_to_values[letter_before]
                    arabic_number += value
                else:
                    value = symbols_to_values[letter]
                    arabic_number += value
                continue
            #  base case if we want to use recursion
            value = symbols_to_values[letter]
            arabic_number += value
            # return arabic_number

        return arabic_number


class TestSolution(unittest.TestCase):
    def test_romanToInt_3(self, s: str) -> int:
        solution = Solution()
        assert 3 == solution.romanToInt("III")

    def test_romanToInt_58(self, s: str) -> int:
        solution = Solution()
        assert 58 == solution.romanToInt("LVIII")

    def test_romanToInt_1994(self, s: str) -> int:
        solution = Solution()
        assert 1994 == solution.romanToInt("MCMXCIV")


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("XXXIV"))
    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
