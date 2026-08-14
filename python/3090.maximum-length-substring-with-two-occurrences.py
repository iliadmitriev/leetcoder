class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        base = ord("a")
        k = 2

        win = [0] * 26
        j = 0
        largest = 0

        for i, ch in enumerate(s):
            win[ord(ch) - base] += 1

            while win[ord(ch) - base] > k:
                win[ord(s[j]) - base] -= 1;
                j += 1

            largest = max(largest, i - j + 1)

        return largest