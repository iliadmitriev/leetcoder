class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        totalAlice = sum(aliceSizes)
        totalBob = sum(bobSizes)

        draw = (totalAlice + totalBob) // 2
        diff = draw - totalAlice

        bobSet = set(bobSizes)

        for alice in aliceSizes:
            bob = diff + alice

            if bob in bobSet:
                return [alice, bob]

        return [0, 0]

