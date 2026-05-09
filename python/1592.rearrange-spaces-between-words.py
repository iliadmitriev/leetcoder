class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        spaces = 0
        j = 0

        for i, ch in enumerate(text):
            if ch != " ":
                continue

            spaces += 1

            if i - j > 0:
                words.append(text[j:i])
            j = i + 1

        if j < len(text):
            words.append(text[j:])

        slots = len(words) - 1
        if slots == 0:
            return words[0] + " " * spaces

        sep = " " * (spaces // slots)
        end = " " * (spaces % slots)

        return sep.join(words) + end

