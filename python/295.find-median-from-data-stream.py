from heapq import heappush, heappop, heappushpop

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.upper) == len(self.lower):
            heappush(self.upper, -heappushpop(self.lower, -num))
        else:
            heappush(self.lower, -heappushpop(self.upper, num))

    def findMedian(self) -> float:
        if len(self.upper) == len(self.lower):
            return (self.upper[0] - self.lower[0]) / 2
        else:
            return self.upper[0]