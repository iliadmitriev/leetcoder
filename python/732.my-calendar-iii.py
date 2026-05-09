from bisect import insort, bisect_left, bisect_right

class MyCalendarThree:

    def __init__(self):
        # all the bookings
        self.data = []
        self.max_active = 0
        

    def book(self, start: int, end: int) -> bool:
        """Add to list using binary search.
        
        n - number of elements
        Time: O(n * log(n))
        Space: O(n)
        
        data - list for storing intervals start and end counts
            on start increase count of overlaping bookings
            on end decrease count of overlaping bookings
            example,
                intervals: [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
                data: [(5,1),(5,1),(10,-1),(10,1),(10,1),(15,-1),(20,-1),(25,1),(40,-1),(50,1),(55,-1),(60,-1)]
        """
        # try to put booking without considering overlaping

        # add statring point of interval with merging
        start_idx = bisect_left(self.data, start, key=itemgetter(0))
        if start_idx < len(self.data) and self.data[start_idx][0] == start:
            self.data[start_idx][1] += 1
        else:
            self.data.insert(start_idx, [start, +1])
        
        # add ending point of interval with merging
        end_idx = bisect_left(self.data, end, key=itemgetter(0))
        if end_idx < len(self.data) and self.data[end_idx][0] == end:
            self.data[end_idx][1] -= 1
        else:
            self.data.insert(end_idx, [end, -1])
        
        active = 0
        # iterate all the booking checking max ovelaping
        for i in range(0, min(end_idx + 1, len(self.data))):
            _, value = self.data[i]
            active += value
            self.max_active = max(self.max_active, active)
            
        return self.max_active if self.max_active else None
        