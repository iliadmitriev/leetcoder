class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def count_trips(total_time: int) -> int:
            return sum(map(lambda x: total_time // x, time))
        
        # left and right time bounds
        left, right = 0, min(time) * totalTrips + 1

        while left < right:
            mid = (left + right) // 2
            if count_trips(mid) < totalTrips:
                left = mid + 1
            else:
                right = mid

        return left