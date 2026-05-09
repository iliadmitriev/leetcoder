class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        dp = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured
        
        for row in range(1, query_row + 1):
            for i in range(row + 1):
                # how much liquid went through left and right ancestor
                left = dp[row - 1][i - 1] if i > 0 else 0
                right = dp[row - 1][i] if i <= row else 0
                # how much extra liquid spilled over 
                left_extra = max(0, left - 1)
                right_extra = max(0, right - 1)
                # take half of left ancestor and half of right ancestor
                # half is because ancestor have two edges to spill extra liquid
                dp[row][i] = left_extra / 2 + right_extra / 2

        return min(1.0, dp[query_row][query_glass])