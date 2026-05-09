from typing import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ch = Counter(s)
        letters = sorted(ch.items(), key=lambda x: x[0])
        res = []

        while letters:
            letter, cnt = letters.pop()
            if cnt > repeatLimit:
                res.append(letter * repeatLimit)

                if not letters:
                    break

                nextLetter, nextCnt = letters.pop()
                res.append(nextLetter)

                nextCnt -= 1
                cnt -= repeatLimit

                if nextCnt > 0:
                    letters.append((nextLetter, nextCnt))
                letters.append((letter, cnt))

            else:
                res.append(letter * cnt)

        return "".join(res)

