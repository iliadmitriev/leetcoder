class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = word.find(ch)
        return word[: pos + 1][::-1] + word[pos + 1 :]

