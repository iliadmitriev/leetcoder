class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(node: int, fuel: int) -> int:
            if fuel < 0:
                return 0

            if node == finish:
                count = 1
            else:
                count = 0

            for next_node, location in enumerate(locations):
                if node == next_node:
                    continue
                count += dp(next_node, fuel - abs(location - locations[node]))
            return count % mod

        return dp(start, fuel)