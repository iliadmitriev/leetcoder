class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total = sum(cost)

        for i in range(2, len(cost), 3):
            total -= cost[i]

        return total

        