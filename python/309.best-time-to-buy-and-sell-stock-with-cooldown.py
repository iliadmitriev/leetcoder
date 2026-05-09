class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Best Time to Buy and Sell Stock with Cooldown.

        Returns:
            maximum profit
        
        3 basic choises:

            1. buy - if there not in transaction
            2. sell and wait 1 day - if there is in transaction
            3. cooldown - always available 

        Time: O(n)
        Space: O(n)
        """
        n = len(prices)
        buy = [0] * n    # bying profit
        sell = [0] * n   # selling profit
        cool = [0] * n   # cooldown profit
        buy[0] = -prices[0]

        for day in range(1, n):
            # buying day profit depends on the choice
            # whether it's a cool down day (then profit stays the same as previous dat)
            # or it's buying day, the day after cooldown 
            # (then profit calculated as previous cooldown day minus current day price)
            buy[day] = max(buy[day - 1], cool[day - 1] - prices[day])
            # selling day profit, is a previous buying day profit plus current day price
            sell[day] = buy[day - 1] + prices[day]
            # cooldown: 2 options
            # 1) profit stays the same as previous day cooldown
            # 2) profit fixed as previous selling day (after preforming transaction sell of buy)
            cool[day] = max(cool[day - 1], sell[day - 1])
        
        # decide between current selling operation, and previous selling (cooldown)
        return max(sell[-1], cool[-1])