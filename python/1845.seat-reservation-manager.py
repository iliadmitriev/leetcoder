import heapq


class SeatManager:

    def __init__(self, n: int):
        self.last = 0
        self.hq = []

    def reserve(self) -> int:
        if not self.hq:
            self.last += 1
            return self.last
        return heapq.heappop(self.hq)
        
    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.last:
            self.last -= 1
        else:
            heapq.heappush(self.hq, seatNumber)
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)