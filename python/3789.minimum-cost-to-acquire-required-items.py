class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total_cost = 0
        if cost1 + cost2 <= costBoth:
            total_cost = need1 * cost1 + need2 * cost2
        else:
            need_both = min(need1, need2)
            total_cost += need_both * costBoth
            
            need1 -= need_both
            need2 -= need_both
            
            total_cost += need1 * min(cost1, costBoth)
            total_cost += need2 * min(cost2, costBoth)
            
        return total_cost
            
            