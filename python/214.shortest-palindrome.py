class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix, suffix = 0, 0

        base = 29
        mod = int(1e9 + 7)
        power = 1

        stack: list[int] = []

        for i, c in enumerate(s):
            ch = ord(c) - ord("a") + 1

            prefix = (prefix * base) % mod
            prefix = (prefix + ch) % mod

            suffix = (suffix + power * ch) % mod
            power = (power * base) % mod

            if suffix == prefix:
                stack.append(i)

        while stack:
            i = stack.pop()
            if s[: i + 1] == s[: i + 1][::-1]:
                leftover = s[i + 1:]
                return leftover[::-1] + s

        return s[1:][::-1] + s

