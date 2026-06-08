class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n = len(nums)
        res = [0] * n 

        # write pointers
        l, r = 0, n - 1

        # read pointers:
        # i - forward pointer
        # j - reverse pointer
        for i in range(n):
            j = n - i - 1 

            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1

            if nums[j] > pivot:
                res[r] = nums[j]
                r -= 1

        # fill the gap with pivot value
        for i in range(l, r + 1):
            res[i] = pivot
          
        return res