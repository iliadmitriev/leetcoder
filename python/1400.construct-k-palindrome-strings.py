class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        if len(s) == k:
            return True

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1

        odd = sum(cnt % 2 for cnt in count)

        return odd <= k

