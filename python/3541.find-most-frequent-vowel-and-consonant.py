

class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt = [0] * 26
        base = ord("a")
        vowels = [ord(ch) - base for ch in "aeiou"]
        maxVowels = 0
        maxConsonants = 0

        for ch in s:
            cnt[ord(ch) - base] += 1

        for i in range(26):
            if i in vowels:
                maxVowels = max(maxVowels, cnt[i])
            else:
                maxConsonants = max(maxConsonants, cnt[i])

        return maxVowels + maxConsonants

