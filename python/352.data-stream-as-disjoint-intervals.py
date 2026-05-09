from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.data = []        

    def addNum(self, value: int) -> None:
        i = bisect_left(self.data, value)
        if i == len(self.data):
            self.data.append(value)
        else:
            if self.data[i] != value:
                self.data.insert(i, value)

    def getIntervals(self) -> List[List[int]]:
        res = []
        for num in self.data:
            if res and (res[-1][1] + 1 == num):
                res[-1][1] = num
            else:
                res.append([num, num])
        return res
        