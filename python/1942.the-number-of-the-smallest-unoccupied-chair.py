import heapq


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:

        n = len(times)
        friends = sorted(list(range(n)), key=lambda x: times[x][0])
        chair = 0  # current not occupied chair
        freeChairs = []  # min heap of freed chairs
        occupiedChairs = []  # min heap of occupied chairs (end time, index)

        for friend in friends:
            start, end = times[friend]

            while occupiedChairs and occupiedChairs[0][0] <= start:
                _, free = heapq.heappop(occupiedChairs)
                if chair == free + 1:
                    chair -= 1
                else:
                    heapq.heappush(freeChairs, free)

            if freeChairs:
                nextChair = heapq.heappop(freeChairs)
            else:
                nextChair = chair
                chair += 1

            if friend == targetFriend:
                return nextChair

            heapq.heappush(occupiedChairs, (end, nextChair))

        return 0

