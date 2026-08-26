class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cur = 0
        cur_len = len(s) + 1
        i, j = 0, 0
        l = 0


        for r in range(len(s)):
            cur += s[r] == "1"

            while (l < r and s[l] == "0") or cur > k:
                cur -= s[l] == "1"
                l += 1

            if cur != k:
                continue
              
            if r - l + 1 < cur_len:
                i, j = l, r + 1
                cur_len = r + 1 - l
            elif r - l + 1 == cur_len and s[l: r + 1] < s[i: j]:
                i, j = l, r + 1
                cur_len = r + 1 - l

        return s[i: j]
