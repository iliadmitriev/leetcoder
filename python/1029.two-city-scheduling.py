class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort array with smaller difference first
        costs = sorted(costs, key=lambda c: c[0] - c[1])
        n = len(costs) // 2
        
        return sum(map(lambda c: c[0], costs[:n])) + sum(map(lambda c: c[1], costs[n:]))