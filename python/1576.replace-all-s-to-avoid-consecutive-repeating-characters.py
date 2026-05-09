class Solution:
    def modifyString(self, s: str) -> str:
        t = list(s)

        for i, ch in enumerate(t):
            if ch != "?":
                continue

            left = t[i - 1] if i > 0 else " "
            right = t[i + 1] if i < len(t) - 1 else " "

            for c in "abc":
                if c != left and c != right:
                    t[i] = c
                    break

        return "".join(t)

