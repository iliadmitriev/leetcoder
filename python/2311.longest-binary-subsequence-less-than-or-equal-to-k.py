class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        taken = 0
        zeros = s.count("0")
        n = len(s)
        cur_len = 0
        cur_val = 0

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                taken += 1
                zeros -= 1
            elif s[i] == "1":
                cur_val += 1 << cur_len

            if cur_val > k:
                return cur_len + zeros

            cur_len += 1

        return n

