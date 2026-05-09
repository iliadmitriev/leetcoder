class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        wordDict = set(wordDict)
        size = sorted(set(map(len, wordDict)))
        
        for i in range(len(s) - 1, -1, -1):
            for j in size:
                if i + j <= len(s) and s[i: i + j] in wordDict and dp[i + j]:
                    dp[i] = dp[i + j]
                    break
                     
                    
        return dp[0]