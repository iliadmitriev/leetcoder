class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[n - 1] == '1':
            return False
            
        dp = [0] * n

        dp[minJump] += 1
        
        if maxJump + 1 < n:
            dp[maxJump + 1] -= 1

        for i in range(1, n):
            dp[i] += dp[i - 1]

            if s[i] == '1' or dp[i] == 0:
                continue

            if i + minJump < n:
                dp[i + minJump] += 1
            if i + maxJump + 1 < n:
                dp[i + maxJump + 1] -= 1

        return dp[n - 1] > 0