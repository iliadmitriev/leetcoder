class Solution:
    def maxPower(self, s: str) -> int:
        res, max_len = 0, 0
        prev = s[0]
        for curr_char in s:
            if curr_char == prev:
                max_len += 1
                res = max(res, max_len)
            else:
                max_len = 1
                prev = curr_char
        return res