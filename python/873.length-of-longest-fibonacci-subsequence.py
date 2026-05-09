

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        maxFibLen = 0

        order = {num: i for i, num in enumerate(arr)}

        def maxFib(a: int, b: int) -> int:

            n = a + b
            if n not in order:
                return 0

            return 1 + maxFib(b, n)

        for i in range(len(arr)):
            for j in range(i):
                maxFibLen = max(
                    maxFibLen,
                    2 + maxFib(arr[j], arr[i]),
                )

        if maxFibLen > 2:
            return maxFibLen

        return 0

