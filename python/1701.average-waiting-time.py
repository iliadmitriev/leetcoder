

class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        n = len(customers)
        totalWait = 0
        idleAt = 0

        for i in range(n):
            start = max(customers[i][0], idleAt)
            totalWait += start - customers[i][0]
            totalWait += customers[i][1]
            idleAt = start + customers[i][1]

        return totalWait / n

