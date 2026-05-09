class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        stack = []
        maxDiff = -1

        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()

            stack.append(num)

            if len(stack) > 1:
                maxDiff = max(maxDiff, stack[-1] - stack[0])

        return maxDiff

