class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # monotonic increasing stack with indexes of elements
        # how many elements current element was the minimum
        MOD = 10**9 + 7
        res = 0
        arr.append(float("-inf"))
        stack = [] # (index, num)

        for i, num in enumerate(arr):

            while stack and num < stack[-1][1]:
                j, prev = stack.pop()

                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + prev * left * right) % MOD

            stack.append((i, num))

        return res