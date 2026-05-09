class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        # optimize 1
        if p == 0:
            return 0

        nums.sort()

        # optimize 2
        if 2 * p == len(nums):
            return max(nums[i + 1] - nums[i] for i in range(0, len(nums) - 1, 2))

        lo, hi = 0, nums[-1] - nums[0]

        def check(nums, mid, p):
            cnt = 0
            i = 0
            while i < len(nums) - 1:
                diff = abs(nums[i + 1] - nums[i])

                if diff <= mid:
                    cnt += 1
                    i += 2
                else:
                    i += 1

                if cnt >= p:
                    return True

            return False

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(nums, mid, p):
                hi = mid
            else:
                lo = mid + 1

        return lo

