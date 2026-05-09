from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()

        cover = 0
        for coin in coins:
            if coin <= cover + 1:
                cover += coin
            else:
                break

        return cover + 1

