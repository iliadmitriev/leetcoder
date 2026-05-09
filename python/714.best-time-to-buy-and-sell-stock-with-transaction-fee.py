class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        Iterative
        
        f - represents expences
        g - represents profits
        
        expenses consist of buying price and fee
        profits consist of selling price 
        
        f(n) = max(f(n - 1), g(n - 1) - price[n] - fee)
        g(n) = max(g(n - 1), f(n - 1) + price[n])
        """
        
        f_1 = -prices[0] - fee
        g_1 = 0
        g = 0
        for i in range(1, len(prices)):
            f = max(f_1, g_1 - prices[i] - fee)
            g = max(g_1, f_1 + prices[i])
            f_1 = f
            g_1 = g
            
        return g