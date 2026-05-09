import heapq


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        count = 0

        min_q, max_q = [], []

        left = -1
        for right in range(len(nums)):

            while min_q and abs(min_q[0][0] - nums[right]) > 2:
                _, left = heapq.heappop(min_q)

            while max_q and abs(max_q[0][0] + nums[right]) > 2:
                _, left = heapq.heappop(max_q)

            heapq.heappush(min_q, (nums[right], right))
            heapq.heappush(max_q, (-nums[right], right))
            count += right - left

        return count

