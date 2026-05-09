class Solution:
    def bisectLeft(self, nums: list[int], target: int, d: int) -> bool:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] < target:
                if target - nums[mid] <= d:
                    return False

                lo = mid + 1
            else:
                if nums[mid] - target <= d:
                    return False

                hi = mid

        return True

    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        res = 0

        for x in arr1:
            if self.bisectLeft(arr2, x, d):
                res += 1

        return res

