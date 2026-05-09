import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        busy = []  # (end, room)
        free = list(range(n))  # (room)
        rooms = [0] * n

        meetings.sort()

        for start, end in meetings:
            # free meetings that is over
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            # no delay
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                ending, room = busy[0]
                duration = end - start
                heapq.heapreplace(busy, (ending + duration, room))

            rooms[room] += 1

        # argmax
        return rooms.index(max(rooms))

