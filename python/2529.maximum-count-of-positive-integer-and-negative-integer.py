class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[-1] < 0:
            return len(nums)

        if nums[0] > 0:
            return len(nums)

        def ins_left(x, arr):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def ins_right(x, arr):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        zero_ins = ins_left(0, nums)
        one_ins = ins_right(0, nums)

        return max(zero_ins, len(nums) - one_ins)