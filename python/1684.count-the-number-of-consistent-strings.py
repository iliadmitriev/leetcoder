class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        def maskChars(s: str) -> int:
            res = 0
            for ch in s:
                res |= 1 << (ord(ch) - 97)
            return res

        allow = maskChars(allowed)
        count = 0

        for word in words:
            mask = maskChars(word)

            if mask & allow == mask:
                count += 1

        return count

