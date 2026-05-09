class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}
        def dp(amount: int, index: int) -> int:
            if (amount, index) in cache:
                return cache[(amount, index)]

            if amount == 0:
                return 1
            if amount < 0 or index >= len(coins):
                return 0

            count = dp(amount - coins[index], index) + dp(amount, index + 1)

            cache[(amount, index)] = count
            return count
        
        return dp(amount, 0)