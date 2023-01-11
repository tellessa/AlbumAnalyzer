class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # length = len(s)
        s.reverse()
        # did not understand initially that s was a LIST, not a str.
        # for initial_letter in s:


sol = Solution()
s = ["h", "e", "l", "l", "o"]
sol.reverseString(s)
print(s)
