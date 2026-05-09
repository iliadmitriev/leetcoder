class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M': 1000}
        pre = None
        sums = 0
        for i in s:
            if pre and pre < maps[i]:
                sums += maps[i] - 2 * pre

            else:
                sums += maps[i]
                pre = maps[i]
        return sums