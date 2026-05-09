class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res = 1 << k
        seen = set()
        for i in range(len(s) - k + 1):
            tpl = s[i:i + k]
            if tpl not in seen:
                res -= 1
                seen.add(tpl)
            if res == 0:
                return True
        return res == 0