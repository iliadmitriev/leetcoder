from collections import Counter


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        total = sum(skill)
        pairs = len(skill) // 2

        if total % pairs != 0:
            return -1

        target = total // pairs
        skillSet = Counter(skill)
        chemistry = 0

        for s, v in skillSet.items():
            if v != skillSet[target - s]:
                return -1

            if s == target - s:
                if v % 2 != 0:
                    return -1
                else:
                    v //= 2

            skillSet[s] = 0
            skillSet[target - s] = 0

            chemistry += s * (target - s) * v

        return chemistry

