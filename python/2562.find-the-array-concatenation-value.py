class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:

        def concat(a: int, b: int) -> int:
            t = b

            while b:
                a *= 10
                b //= 10

            return a + t

        i, j = 0, len(nums) - 1

        res = 0
        while i < j:

            res += concat(nums[i], nums[j])
            i += 1
            j -= 1

        if i == j:
            res += nums[i]

        return res

