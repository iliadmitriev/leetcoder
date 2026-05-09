class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        p = Counter(chars)
        res = 0
        for word in words:
            if len(word) > len(chars):
                continue

            w = Counter(word)
            if all(cnt <= p[ch] for ch, cnt in w.items()):
                res += len(word)

        return res