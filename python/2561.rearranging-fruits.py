import collections


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        cost = 0
        freq = collections.Counter()
        swap = []

        for fruit in basket1:
            freq[fruit] += 1

        for fruit in basket2:
            freq[fruit] -= 1

        min_fruit = min(freq)

        for fruit, cnt in freq.items():
            if cnt % 2 != 0:
                return -1

            swap.extend([fruit] * (abs(cnt) // 2))

        if not swap:
            return 0

        swap.sort()

        # first half of smallest fruits
        for i in range(len(swap) // 2):
            cost += min(2 * min_fruit, swap[i])

        return cost

