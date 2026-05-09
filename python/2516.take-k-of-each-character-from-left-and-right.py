

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = [0] * 3
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        A, B, C = cnt[0] - k, cnt[1] - k, cnt[2] - k

        if A < 0 or B < 0 or C < 0:
            return -1

        maxLen = 0
        n = len(s)
        i, j = 0, 0
        a, b, c = 0, 0, 0

        while i < n:
            a += s[i] == "a"
            b += s[i] == "b"
            c += s[i] == "c"

            while a > A or b > B or c > C:
                a -= s[j] == "a"
                b -= s[j] == "b"
                c -= s[j] == "c"
                j += 1

            maxLen = max(maxLen, i - j + 1)

            i += 1

        return n - maxLen

