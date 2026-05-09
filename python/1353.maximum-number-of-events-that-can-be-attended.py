import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        n = len(events)
        max_events = 0
        i = 0  # current event index
        heap = []  # events end time min heap (to attend first event with earliest end time)

        events.sort()

        day = 1

        while i < n or heap:
            if not heap:
                day = events[i][0]

            # find all events that can be possibly attended on current day
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            heapq.heappop(heap)
            max_events += 1
            day += 1

            # remove all events that can't be attended
            while heap and heap[0] < day:
                heapq.heappop(heap)

        return max_events

