import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = 0
        heapq.heapify(nums)

        while len(nums) > 1 and nums[0] < k:
            n += 1
            a, b = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, 2 * a + b)

        return n

