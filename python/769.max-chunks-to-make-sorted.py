

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        chunks = 0

        curMax = -1

        for i, num in enumerate(arr):
            curMax = max(curMax, num)

            if curMax == i:
                chunks += 1

        return chunks

