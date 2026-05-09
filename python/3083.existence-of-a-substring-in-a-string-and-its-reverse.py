class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]
        r = set()
        for i in range(len(rev) - 1):
            r.add(rev[i: i + 2])

        for i in range(len(s) - 1):
            if s[i: i + 2] in r:
                return True

        return False

