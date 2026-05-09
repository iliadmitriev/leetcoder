class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Regular expression match

        given string   s = 'xaabyc'
        given pattern  p = 'xa*b.c'

        dp:
                0  1  2  3  4  5  6
                   x  a  *  b  .  c
          0     t  f  f  f  f  f  f
          1  x  f  t  f  t  f  f  f
          2  a  f  f  t  t  f  f  f
          3  a  f  f  f  t  f  f  f
          4  b  f  f  f  f  t  f  f
          5  y  f  f  f  f  f  t  f
          6  c  f  f  f  f  f  f  t
                                 --

        result: True (bottom right corner)

        * Time: O(m * n), m - string length, n - pattern length
        * Space: O(m * n)

        :param s: given text string
        :param p: given pattern
        :return: true is text string matches pattern
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True

        # build first row
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
            else:
                dp[0][j] = False

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # literal case
                if p[j - 1].isalpha():
                    # if literals match then copy value from top-left cell [i - 1][j - 1]
                    dp[i][j] = (p[j - 1] == s[i - 1]) and dp[i - 1][j - 1]

                # dot case
                elif p[j - 1] == '.':
                    # dot matches any symbol,
                    # then just copy value from top-left cell [i - 1][j - 1]
                    dp[i][j] = dp[i - 1][j - 1]

                # asterisk case
                else:
                    # if pattern literal to the left of asterisk
                    # matches with string literal or
                    # pattern literal is `.` (matches any literal)
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        # case: zero or more occurrences
                        # check value two steps back [i][j - 2] from current cell,
                        # then copy value from top cell [i - 1][j]
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        # otherwise (there is no match)
                        # copy value from two steps back [i][j - 2]
                        dp[i][j] = dp[i][j - 2]

        return dp[m][n]
