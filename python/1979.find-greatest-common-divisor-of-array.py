class Solution:
    def findGCD(self, nums: list[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while a != b:
                if a > b:
                    a -= b
                else:
                    b -= a
            return a

        return gcd(max(nums), min(nums))

