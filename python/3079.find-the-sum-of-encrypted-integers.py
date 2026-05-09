class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        def encrypt(num: int) -> int:
            maxDigit = 0
            counter = 0
            while num:
                num, digit = divmod(num, 10)
                maxDigit = max(maxDigit, digit)
                counter += 1

            res = 0
            for _ in range(counter):
                res = res * 10 + maxDigit

            return res

        return sum(encrypt(num) for num in nums)

