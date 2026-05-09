class Solution:
    @staticmethod
    def getChildCount(cur: int, n: int) -> int:
        """Count the number of children between siblings.

        cur = 2, limit = 2500
        2 .. 3 -> 1
        20 .. 30 -> 10
        200 .. 300 -> 100
        2000 .. 2501 -> 501

        res = 1 + 10 + 100 + 501 = 612
        """
        res = 0

        bound = cur + 1

        while cur <= n:
            # count the number of children between siblings
            res += bound - cur

            # move pointer down to the child node, with limit (inclusively)
            bound = min(bound * 10, n + 1)
            # move pointer down to the child node
            cur *= 10

        return res

    def findKthNumber(self, n: int, k: int) -> int:
        i = 1  # position
        cur = 1  # value

        while i < k:
            count = Solution.getChildCount(cur, n)

            # if position i + count covers k (includes solution)
            # move pointer down to children node to find the solution
            if i + count > k:
                cur *= 10
                i += 1
            else:
                # otherwise, move position ponter left to the sibling node
                cur += 1
                i += count  # add the number of children between siblings

        return cur

