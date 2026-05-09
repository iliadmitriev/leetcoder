class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        i = 0

        while num2 > 0:
            i += num1 // num2
            num1, num2 = num2, num1 % num2

        return i

