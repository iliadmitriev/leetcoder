class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        res = []
        groupCur = 0
        posToGroup = [-1] * n
        groupStart = [0]

        cache = sorted(enumerate(nums), key=lambda x: x[1])
        prev = cache[0][1]

        for j, (i, num) in enumerate(cache):
            if num - prev > limit:
                groupCur += 1
                groupStart.append(j)

            posToGroup[i] = groupCur
            prev = num

        for i, num in enumerate(nums):
            group = posToGroup[i]
            res.append(cache[groupStart[group]][1])
            groupStart[group] += 1

        return res

