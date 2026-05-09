class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        n = len(energy)
        prefix = [0] * n

        for i in range(n):
            prefix[i] = energy[i]

            if i - k >= 0:
                prefix[i] = max(prefix[i], prefix[i] + prefix[i - k])

        return max(prefix[-k:])

