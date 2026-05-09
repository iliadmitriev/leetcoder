from functools import cache


class Solution:
    @cache
    def calcPrimeScore(self, num: int) -> int:
        """Prime score is the number off all distinct prime number in given number."""
        score = 0

        if num % 2 == 0:
            score += 1

        while num % 2 == 0:
            num //= 2

        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                score += 1

            while num % i == 0:
                num //= i

        if num > 2:
            score += 1

        return score

    def maximumScore(self, nums: list[int], k: int) -> int:
        result = 1
        MOD = int(1e9 + 7)
        n = len(nums)
        ordered = sorted(enumerate(nums), key=lambda x: x[1])
        scores = [self.calcPrimeScore(num) for num in nums]
        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        while ordered and k > 0:
            index, num = ordered.pop()

            l, r = index - left[index], right[index] - index

            step = min(k, l * r)
            result *= pow(num, step, MOD)
            result %= MOD
            k -= step

        return result

