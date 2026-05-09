class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        for cost in costs:
            if cost > coins:
                break
            coins -= cost
            count += 1
        return count