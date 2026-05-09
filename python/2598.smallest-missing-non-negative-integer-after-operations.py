

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        if value == 1:
            return len(nums)

        freq = [0] * value

        for num in nums:
            freq[num % value] += 1

        full = min(freq)
        i = freq.index(full)

        return full * value + i

