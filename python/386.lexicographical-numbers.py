class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        cur = 1

        for _ in range(n):
            res.append(cur)

            # if there is child nodes, then step down 17 -> 170
            if cur * 10 <= n:
                cur *= 10
            else:
                # otherwise, if reached last child sibling node,
                # then step up to the parent node 179 -> 17
                # or if there is no sibling, go to parent
                while cur % 10 == 9 or cur + 1 > n:
                    cur //= 10

                # go to sibling
                cur += 1

        return res

