import heapq


class NumberContainers:

    def __init__(self):
        self.nums = {}  # ind -> num
        self.inx = {}  # num -> indexes

    def change(self, index: int, number: int) -> None:
        self.nums[index] = number

        hq = self.inx.setdefault(number, [])
        heapq.heappush(hq, index)

    def find(self, number: int) -> int:
        if not self.inx.get(number):
            return -1

        while self.inx.get(number):

            index = self.inx[number][0]

            if self.nums.get(index) == number:
                return index

            heapq.heappop(self.inx[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)