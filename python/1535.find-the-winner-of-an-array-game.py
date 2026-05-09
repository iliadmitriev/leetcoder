class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curMax = arr[0]
        curCnt = 0

        for i in range(1, len(arr)):
            if curMax > arr[i]:
                curCnt += 1
            else:
                curCnt = 1
                curMax = arr[i]

            if curCnt == k:
                return curMax

        return curMax