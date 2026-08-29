class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        res = [0] * n

        indexed = sorted((v, i) for i, v in enumerate(nums)) # [(value, position), ...]
        values = [indexed[0][0]]
        group = [indexed[0][1]]


        def drain(res: list[int], group: list[int], values: list[int]) -> None:
            for k, j in enumerate(sorted(group)):
                res[j] = values[k]

        for i in range(1, n):
            if indexed[i][0] - indexed[i - 1][0] <= limit:
                values.append(indexed[i][0]) # value
                group.append(indexed[i][1]) # position
            else:
                drain(res, group, values)
                values = [indexed[i][0]]
                group = [indexed[i][1]]

        drain(res, group, values)

        return res