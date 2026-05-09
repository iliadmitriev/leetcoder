class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        n = len(nums)
        srt = []

        prev = 0
        prevBits = nums[0].bit_count()
        for i in range(n):
            if prevBits != nums[i].bit_count():
                srt.extend(sorted(nums[prev:i]))
                prevBits = nums[i].bit_count()
                prev = i

        if prev < n:
            srt.extend(sorted(nums[prev:]))

        return srt == sorted(nums)

