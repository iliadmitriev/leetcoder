import bisect
import collections


class Router:
    def __init__(self, memoryLimit: int):
        self.data = collections.deque()  # tuples (source, destination, timestamp)
        self.limit = memoryLimit
        self.cache = {}  # tuples (source, destination, timestamp): bool
        self.counter = {}  # destination: deque[time]

    def _add_counter(self, destination: int, timestamp: int):
        if destination not in self.counter:
            dest = []
            self.counter[destination] = dest
        else:
            dest = self.counter[destination]

        dest.append(timestamp)

    def _remove_counter(self, destination: int, timestamp: int):
        dest = self.counter[destination]

        left = bisect.bisect_left(dest, timestamp)

        if dest[left] == timestamp:
            left += 1

        self.counter[destination] = dest[left:]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.cache:
            return False

        if len(self.data) == self.limit:
            old = self.data.popleft()
            del self.cache[old]
            self._remove_counter(old[1], old[2])

        self.data.append(packet)
        self.cache[packet] = True
        self._add_counter(destination, timestamp)

        return True

    def forwardPacket(self) -> list[int]:
        if not self.data:
            return []

        packet = self.data.popleft()
        del self.cache[packet]
        self._remove_counter(packet[1], packet[2])

        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.counter:
            return 0

        dest = self.counter[destination]
        left = bisect.bisect_left(dest, startTime)
        right = bisect.bisect_right(dest, endTime)

        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)