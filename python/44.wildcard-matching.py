class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Match pattern and string and return true if them matches
        
        pattern can contain:
        
        `*` - 0 or many any literal symbols
        `?` - any literal symbol
        
        n - length of input text string
        m - lenght of input pattern
        
        
        dp:
        
           j  0  1  2  3  4  5
        i        x  ?  y  *  z
        0     t  f  f  f  f  f
        1  x  f  t  f  f  f  f
        2  a  f  f  t  f  f  f
        3  y  f  f  f  t  t  f
        4  l  f  f  f  f  t  f
        5  m  f  f  f  f  t  f
        6  z  f  f  f  f  t  t
                            ---
        Time: O(m x n)
        Space: O(m x n)
        
        :param s: given string
        :param p: given pattern
        :return: true if string matches pattern
        """
        
        n = len(s)  # i, rows
        m = len(p)  # j, columns
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = False
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if literal symbols match
                # or pattern has `?` at current position (matches any)
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    # copy value from top left cell of grid
                    dp[i][j] = dp[i - 1][j - 1]
                # if current symbol is asterisk
                elif p[j - 1] == '*':
                    # we check value left of the current cell
                    # and top of the current cell
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
        
        return dp[n][m]