class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        cache = [0] * 101
        count = 0

        for num in nums:
            if num < k:
                return -1

            cache[num] += 1

            if cache[num] == 1:
                count += 1

        if cache[k] > 0:
            return count - 1

        return count

