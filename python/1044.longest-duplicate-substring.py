class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def robinKarp(s: str, maxLen: int) -> str:
            mod = 1000000000039
            shift = ord("a") - 1
            base = 29
            prefix = 0
            upperBase = pow(base, maxLen - 1, mod)

            for i in range(maxLen):
                prefix = (prefix * base + ord(s[i]) - shift) % mod

            seen: set[int] = {prefix}

            for i in range(maxLen, len(s)):
                prefix = (mod + prefix - upperBase * (ord(s[i - maxLen]) - shift)) % mod
                prefix = (prefix * base + ord(s[i]) - shift) % mod
                if prefix in seen:
                    return s[i - maxLen + 1: i + 1]
                seen.add(prefix)

            return ""

        lo, hi = 1, len(s)
        res = ""

        while lo < hi:
            mid = (lo + hi) // 2

            substr = robinKarp(s, mid)

            if substr:
                res = substr
                lo = mid + 1
            else:
                hi = mid

        return res

