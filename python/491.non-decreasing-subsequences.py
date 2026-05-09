class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(start: int, curr: List[int]):
            if len(curr) > 1:
                res.append(curr.copy())

            last = curr[-1] if curr else -inf
            seen = set()
            for i in range(start, n):
                if nums[i] not in seen and nums[i] >= last:
                    curr.append(nums[i])
                    backtrack(i + 1, curr)
                    curr.pop()
                    seen.add(nums[i])

        backtrack(0, [])
        return res