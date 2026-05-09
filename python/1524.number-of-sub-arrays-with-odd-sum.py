class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MMOD = int(1e9) + 7
        odd, even = 0, 0

        for num in arr:
            if num % 2:
                odd, even = even + 1, odd
            else:
                even += 1

        return odd * (1 + even) % MMOD

