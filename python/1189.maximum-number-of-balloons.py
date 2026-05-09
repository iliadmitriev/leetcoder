class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = [0] * 26
        for c in text:
            count[ord(c) - ord("a")] += 1

        res = len(text)
        res = min(res, count[1])
        res = min(res, count[0])
        res = min(res, count[11] // 2)
        res = min(res, count[14] // 2)
        res = min(res, count[13])

        return res

