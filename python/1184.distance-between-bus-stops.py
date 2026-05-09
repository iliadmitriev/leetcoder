class Solution:
    def distanceBetweenBusStops(
        self, distance: list[int], start: int, destination: int
    ) -> int:
        total = sum(distance)
        if start > destination:
            start, destination = destination, start

        diff = sum(distance[start:destination])

        return min(diff, total - diff)

