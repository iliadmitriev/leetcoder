

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        shift = ord("a")
        for ch in word:
            freq[ord(ch) - shift] += 1

        freq.sort(reverse=True)

        return (
            sum(freq[:8])
            + 2 * sum(freq[8:16])
            + 3 * sum(freq[16:24])
            + 4 * sum(freq[24:])
        )

