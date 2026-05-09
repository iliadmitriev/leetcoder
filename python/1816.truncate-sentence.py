class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = 0
        cut = len(s)

        for i in range(len(s)):

            if s[i] == " ":
                words += 1

            if words == k:
                cut = i
                break

        return s[:cut]

