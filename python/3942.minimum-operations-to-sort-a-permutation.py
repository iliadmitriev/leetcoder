class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        shift = nums.index(0)
        asc, desc = True, True

        for i in range(1, n):
            j = (i + shift) % n

            if nums[j] != i:
                asc = False
            if nums[j] != n - i:
                desc = False

            # early return when unable to sort
            if not asc and not desc:
                return -1
    
        # [1,2,3,4,0] -> [2,3,4,0,1] -> [3,4,0,1,2] -> [4,0,1,2,3] -> [0,1,2,3,4]
        # [1,2,3,4,0] -> [0,4,3,2,1] -> [4,3,2,1,0] -> [0,1,2,3,4]
        if asc:
            return min(shift, n - shift + 2)

        return min(n - shift, shift + 2)
