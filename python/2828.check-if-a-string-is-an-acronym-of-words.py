class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False

        for i, ch in enumerate(s):
            if not words[i] or ch != words[i][0]:
                return False

        return True

