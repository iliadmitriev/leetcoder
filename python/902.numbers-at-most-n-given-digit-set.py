class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        str_n = str(n)
        l = len(str_n)
        
        dp = [0] * (l + 1)
        dp[0] = 1
        
        for i in range(1, l + 1):
            for digit in digits:
                if digit < str_n[l - i]:
                    dp[i] += len(digits) ** (i - 1)
                elif digit == str_n[l - i]:
                    dp[i] += dp[i - 1]

        summ = sum(len(digits) ** i for i in range(1, l))
                
        return dp[l] + summ