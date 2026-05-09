class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ops = 0

        stack = [0]

        for num in nums:
            while stack[-1] > num:
                stack.pop()

            if stack[-1] == num:
                continue

            stack.append(num)
            ops += 1

        return ops

