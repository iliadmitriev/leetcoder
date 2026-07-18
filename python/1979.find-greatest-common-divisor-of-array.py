class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        return gcd(max(nums), min(nums))