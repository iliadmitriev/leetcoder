class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        counts = [0] * (max_cost + 1)
        bars = 0

        for cost in costs:
            counts[cost] += 1

        for cost in range(1, max_cost + 1):
            if counts[cost] == 0:
                continue

            can_buy = min(coins // cost, counts[cost])
            bars += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return bars
