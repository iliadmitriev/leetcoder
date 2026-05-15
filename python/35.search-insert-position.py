class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bs(lo, hi):
            if lo == hi:
                return lo

            mid = (lo + hi) // 2

            if nums[mid] < target:
                return bs(mid + 1, hi)
            else:
                return bs(lo, mid)
        
        return bs(0, len(nums))
