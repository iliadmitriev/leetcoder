class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vow = curr = sum(1 for i in range(k) if s[i] in vowels)
        for i in range(k, len(s)):
            curr -= s[i - k] in vowels
            curr += s[i] in vowels
            max_vow = max(curr, max_vow)

        return max_vow