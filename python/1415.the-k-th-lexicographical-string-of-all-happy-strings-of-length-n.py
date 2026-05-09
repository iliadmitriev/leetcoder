class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def backtrack(prev: str, cur: list[str], n: int, k: int, pos: list[int]) -> str:
            if len(cur) == n:
                pos[0] += 1

                if pos[0] == k:
                    return "".join(cur)

                return ""

            for c in "abc":
                if c == prev:
                    continue

                cur.append(c)
                res = backtrack(c, cur, n, k, pos)
                if res:
                    return res
                cur.pop()

            return ""

        return backtrack("", [], n, k, [0])

