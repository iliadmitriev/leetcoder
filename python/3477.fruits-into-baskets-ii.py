class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        left = len(baskets)

        for fruit in fruits:
            for j in range(len(baskets)):
                if fruit <= baskets[j]:
                    baskets[j] = -1
                    left -= 1
                    break

        return left

