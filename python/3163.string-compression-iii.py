class Solution:
    def compressedString(self, word: str) -> str:
        prev = ""
        count = 0
        res = []

        for ch in word:
            if ch == prev and count < 9:
                count += 1
            else:
                if prev:
                    res.append(str(count))
                    res.append(prev)
                count = 1

            prev = ch

        if prev:
            res.append(str(count))
            res.append(prev)

        return "".join(res)

