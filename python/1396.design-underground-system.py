class UndergroundSystem:

    def __init__(self):
        self.check = {}  # id -> (start, start time)
        self.stat = {}  # start*end -> (total time, total count)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.check.pop(id, (0, 0))
        key = self.__key(start, stationName)
        total, count = self.stat.get(key, (0, 0))
        self.stat[key] = (total + t - time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = self.__key(startStation, endStation)
        total, count = self.stat.get(key, (0, 1))
        return total / count

    def __key(self, start: str, end: str) -> str:
        return (start, end)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)