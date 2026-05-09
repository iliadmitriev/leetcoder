class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        total = 0

        happiness.sort(reverse=True)

        for j in range(k):
            value = max(0, happiness[j] - j)

            if value == 0:
                break

            total += value

        return total

