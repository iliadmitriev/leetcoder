from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        counter = [0] * (n + 1)

        for num in nums:
            idx = min(num, n)
            counter[idx] += 1

        right = 0
        for i in range(len(counter) - 1, -1, -1):
            right += counter[i]
            if i == right:
                return i

        return -1

