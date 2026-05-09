class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            sign = 1
            i += 1
        while i < n and s[i] == '0':
            i += 1
        j = 0
        while j < 11 and i + j < n and s[i + j].isdigit():
            res *= 10
            res += (ord(s[i + j]) - 48)
            j += 1
        res *= sign
        if res < ~(1 << 31) + 1:
            return ~(1 << 31) + 1
        elif res > (1 << 31) - 1:
            return (1 << 31) - 1
        return res
