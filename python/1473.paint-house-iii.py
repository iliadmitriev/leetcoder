class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """Count minimal paint cost.
        
        Args:
            houses (list of int): list of houses
            n (int): number of colors (1 - indexed)
            m (int): number of houses
            target (int): limit of maximum neigbours
        
        Time: O(m * n)
        Space: O(m * n)
        """

        @cache
        def dp(i: int, c: int, t: int) -> int:
            """
            Args:
                i (int): current house index
                c (int): color of previous house
                t (int): current heighbourhoods count
            """            
            if t < 0:
                return float('inf')

            if i == m:
                return 0 if t == 0 else float('inf')
            
            if houses[i]:
                # if current house is already painted
                # just save next i + 1 house
                ans = dp(i + 1, houses[i], t - int(houses[i] != c))
            else:
                # if current house is not painted
                # try to paint with any color available colors
                # and choose min of the total cost
                ans = min(
                    cost[i][k - 1] + dp(i + 1, k, t - int(k != c))
                    for k in range(1, n + 1)
                )
                
            return ans
        
        res = dp(0, 0, target)
        return res if res < float('inf') else -1