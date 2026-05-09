class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        res = set()
        cur = set([0])

        for x in arr:
            cur = {x | y for y in cur}
            cur.add(x)

            res.update(cur)

        return len(res)

