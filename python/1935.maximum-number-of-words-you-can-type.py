class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # return sum(all(ch not in brokenLetters for ch in word) for word in text.split())
        
        n = len(text)
        ALPHA = 26
        BASE = ord("a")
        SEP = " "
        broken = [1] * ALPHA

        for ch in brokenLetters:
            broken[ord(ch) - BASE] = 0

        i = 0
        cur = 1
        count = 0

        for j, ch in enumerate(text):
            if text[j] != SEP:
                cur &= broken[ord(ch) - BASE]
                continue

            if i < j:
                count += cur
                cur = 1
                i = j + 1

        if i < n:
            count += cur

        return count
