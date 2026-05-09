class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def rle(s: str) -> list[tuple[str, int]]:
            res = []
            cnt, pre = 0, ""

            for ch in s:
                if ch == pre:
                    cnt += 1
                else:
                    res.append((pre, cnt))
                    cnt = 1
                    pre = ch

            if pre:
                res.append((pre, cnt))

            return res

        name1, typed1 = rle(name), rle(typed)

        if len(name1) != len(typed1):
            return False

        for (a, c1), (b, c2) in zip(name1, typed1):
            if a != b:
                return False
            if c1 > c2:
                return False

        return True

