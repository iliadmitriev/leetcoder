class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        indices = [i for i, n in enumerate(nums) if n == key]
        res = []
        n = len(nums)
        prev = 0

        for i in indices:
            left = max(prev, i - k)
            right = min(n, i + k + 1)

            res.extend(range(left, right))

            prev = right

        return res

