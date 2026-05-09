class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        length = 10
        if len(s) < length:
            return []

        base = 7

        code = {"A": 1, "C": 2, "G": 3, "T": 4}

        power = base ** (length - 1)
        prefix = 0

        for i in range(length):
            prefix *= base
            prefix += code[s[i]]

        res: list[str] = []
        seen: set[int] = set([prefix])
        alreadySeen: set[int] = set()

        for i in range(length, len(s)):
            prefix -= power * code[s[i - length]]
            prefix *= base
            prefix += code[s[i]]

            if prefix in seen and prefix not in alreadySeen:
                res.append(s[i - length + 1: i + 1])
                seen.discard(prefix)
                alreadySeen.add(prefix)

            seen.add(prefix)

        return res

