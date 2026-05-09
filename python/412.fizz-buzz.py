class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []

        for i in range(n):
            x = i + 1

            if x % 3 == 0 and x % 5 == 0:
                res.append("FizzBuzz")
            elif x % 3 == 0:
                res.append("Fizz")
            elif x % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(x))

        return res

