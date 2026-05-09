class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # no need to take bus at all
        if source == target:
            return 0

        # build graph of stop -> set of buses
        gr = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                gr[stop].add(bus)
        
        queue = deque([(source, 0)])
        vis_stops = set()
        vis_buses = set()

        while queue:
            stop, dist = queue.popleft()

            if stop == target:
                return dist

            for bus in gr[stop]:
                if bus in vis_buses:
                    continue
                vis_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop in vis_stops:
                        continue
                    vis_stops.add(next_stop)

                    queue.append((next_stop, dist + 1))

        return -1