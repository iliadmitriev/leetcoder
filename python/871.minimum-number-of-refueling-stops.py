class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Idea: Wayback machine
        
        1. Fastforward to the maximum reachable gas station with current amount of gas.
        2. If has reached the target - return number of stations
        3. Otherwise go back in time and choose station with maximum reserve of fuel (increasing number of stations):
            - if it's enough continue move forward
            - otherwise chose more stations (with maximum amount of fuel and increase number of stations)
            - if run out of station and still not enought, return -1 (unable to get to target)
        
        Time: O(n * log(n))
        Space: O(n)
        """
        fuel = startFuel
        count = 0 # count of stations used for refueling
        i = 0 # current station index
        n = len(stations)
        hq = [] # heap queue to store maximum of gas stations reserves
        
        while fuel < target:
            
            # check if we have enough fuel to cover distance
            while i < n and fuel >= stations[i][0]:
                # add station reserves to heap
                heapq.heappush(hq, -stations[i][1])
                # fastforward to next station
                i += 1
                        
            if not hq:
                return -1
            
            top = -heapq.heappop(hq)
            fuel += top
            count += 1
            
        return count