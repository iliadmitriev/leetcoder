class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:

        def intersect(x: list[int], y: list[int]) -> list[int]:
            _x = set(x)

            return [v for v in y if v in _x]

        res = nums[0]
        for i in range(1, len(nums)):
            res = intersect(res, nums[i])

            # optimize
            if not res:
                return []

        return sorted(res)

