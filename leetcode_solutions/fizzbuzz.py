class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        def parse(n):
            if n % 3 == 0:
                if n % 5 == 0:
                    return "FizzBuzz"
                return "Fizz"
            elif n % 5 == 0:
                return "Buzz"
            else:
                return str(n)

        numbers = [i for i in range(1, n + 1)]
        return list(map(parse, numbers))


inputs = [3, 5, 15]
sol = Solution()
for i in inputs:
    res = sol.fizzBuzz(i)
    print(res)
