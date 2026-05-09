class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1
        n = len(digits) - 1

        while n >= 0 and carry:
            carry, digits[n] = divmod(digits[n] + carry, 10)
            n -= 1

        if carry:
            digits = [1] + digits

        return digits

