class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        base = ord("a")
        
        cnt = [0] * 26
        for i in range(n // 2):
            cnt[ord(s[i]) - base] += 1

        mid = ""
        if n % 2 == 1:
            mid = s[n // 2]

        half = "".join(c * k for c, k in zip(ascii_lowercase, cnt))

        left = "".join(half)
        right = left[::-1]

        return f"{left}{mid}{right}"
        