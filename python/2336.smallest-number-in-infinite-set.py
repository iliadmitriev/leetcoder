from heapq import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self._counter = 0
        self._set = set()
        self._hq = []

    def popSmallest(self) -> int:
        if len(self._hq):
            smallest = heappop(self._hq)
            self._set.remove(smallest)
            return smallest

        self._counter += 1
        return self._counter
        

    def addBack(self, num: int) -> None:
        if num <= self._counter and num not in self._set:
            heappush(self._hq, num)
            self._set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)