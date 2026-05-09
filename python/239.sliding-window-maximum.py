class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        res = []

        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(i)

            if i < k - 1:
                continue

            res.append(nums[queue[0]])

            if queue[0] == i - k + 1:
                queue.popleft()

        return res