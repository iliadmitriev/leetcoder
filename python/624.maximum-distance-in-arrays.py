class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        maxItem = arrays[0][-1]
        minItem = arrays[0][0]

        res = 0

        for i in range(1, len(arrays)):
            res = max(
                res,
                max(
                    arrays[i][-1] - minItem,
                    maxItem - arrays[i][0],
                ),
            )

            maxItem = max(maxItem, arrays[i][-1])
            minItem = min(minItem, arrays[i][0])

        return res

