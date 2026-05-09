class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        maxSub = 0

        # fist minimum, second minimum
        bmin1, bmin2 = [n + 1] * (n + 1), [n + 1] * (n + 1)

        for u, v in conflictingPairs:
            a, b = min(u, v), max(u, v)

            if bmin1[a] > b:
                bmin2[a] = bmin1[a]
                bmin1[a] = b

            elif bmin2[a] > b:
                bmin2[a] = b

        ib1 = n
        b2 = n + 1
        delCount = [0] * (n + 1)

        for i in range(n, 0, -1):
            if bmin1[ib1] > bmin1[i]:
                b2 = min(b2, bmin1[ib1], bmin2[i])
                ib1 = i
            else:
                b2 = min(b2, bmin1[i])

            maxSub += bmin1[ib1] - i
            delCount[ib1] += b2 - bmin1[ib1]

        return maxSub + max(delCount)

