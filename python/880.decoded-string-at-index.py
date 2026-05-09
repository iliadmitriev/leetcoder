class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        stack = []
        for sym in s:
            if sym.isalpha():
                length += 1
            elif sym.isdigit():
                length *= int(sym)

        for sym in reversed(s):
            k %= length

            if k==0 and sym.isalpha():
                return sym
            elif sym.isdigit():
                length /= int(sym)
            else:
                length -= 1

        return ""
