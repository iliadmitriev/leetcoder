import itertools


class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        n = len(skill)
        m = len(mana)

        # convert skill to prefix sum of start time
        start = list(itertools.accumulate(skill, initial=0))
        # convert skill to prefix sum of end time
        end = list(itertools.accumulate(skill))

        shift = 0
        totalShift = 0

        for prev, cur in itertools.pairwise(mana):
            # count max possible time shift for current mana production
            # depending on previous mana end time (free worker)
            shift = max(e * prev - s * cur for s, e in zip(start, end))

            totalShift += shift

        return totalShift + end[n - 1] * mana[m - 1]

