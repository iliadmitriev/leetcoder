class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        """
        cases:
        1. k = 0: return 0
        2. k = 1: return max(i, (weights[0] + weights[i]) + (weights[i+1] + weights[n-1])) -
                           min(j, (weights[0] + weights[j]) + (weights[j+1] + weights[n-1]))

                           j, i = 0 to n - 1
        ....
        n. k = len(weights): return 0
        """
        n = len(weights)
        if k == 1 or k == n:
            return 0

        w_pairs = [weights[i] + weights[i + 1] for i in range(n - 1)]
        w_pairs.sort()

        k -= 1
        return sum(w_pairs[-k:]) - sum(w_pairs[:k])

