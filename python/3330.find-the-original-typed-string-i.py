class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1

        prev = ""

        for char in word:
            if char == prev:
                total += 1
            prev = char

        return total

