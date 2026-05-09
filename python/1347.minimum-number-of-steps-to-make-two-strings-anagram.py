class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c = {}
        for ch in s:
            c[ch] = c.get(ch, 0) + 1

        for ch in t:
            if ch not in c:
                continue

            c[ch] -= 1

            if c[ch] == 0:
                del c[ch]

        return sum(c.values())