import collections


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        count = collections.defaultdict(int)
        j = 0
        maxFruit = 0

        for i in range(n):
            count[fruits[i]] += 1

            while len(count) > 2:
                count[fruits[j]] -= 1

                if count[fruits[j]] == 0:
                    del count[fruits[j]]

                j += 1

            maxFruit = max(maxFruit, i - j + 1)

        return maxFruit

