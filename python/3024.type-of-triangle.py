class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a, b, c = sorted(nums)
        if c >= a + b:
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c or c == a:
            return "isosceles"

        return "scalene"

