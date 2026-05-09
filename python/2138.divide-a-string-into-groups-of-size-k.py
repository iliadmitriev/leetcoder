class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        res = [s[i : i + k] for i in range(0, len(s), k)]
        if len(res[-1]) < k:
            res[-1] += fill * (k - len(res[-1]))

        return res

