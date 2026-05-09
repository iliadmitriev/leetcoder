class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        prev = -1
        poisoned = 0

        for tm in timeSeries:

            if prev == -1 or tm >= prev + duration:
                poisoned += duration
            else:
                poisoned += tm - prev

            prev = tm

        return poisoned

