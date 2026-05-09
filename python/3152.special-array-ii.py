

class Solution:
    @staticmethod
    def searchLeft(nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo

    @staticmethod
    def searchRight(nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1

        return lo

    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(queries)
        result = [True] * n

        prefix = []
        prev = (nums[0] + 1) % 2

        for i, num in enumerate(nums):
            if prev + (num % 2) != 1:
                prefix.append(i)
            prev = num % 2

        for i, (left, right) in enumerate(queries):
            if left < right:
                idxLeft = self.searchRight(prefix, left)
                idxRight = self.searchRight(prefix, right)
                result[i] = idxLeft == idxRight

        return result

