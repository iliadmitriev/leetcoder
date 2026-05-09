class MyCalendarTwo:
    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new event overlaps with any double booking
        for double_start, double_end in self.double_bookings:
            if start < double_end and end > double_start:
                return False
        
        # Check if the new event overlaps with any single booking
        for single_start, single_end in self.single_bookings:
            if start < single_end and end > single_start:
                self.double_bookings.append((max(start, single_start), min(end, single_end)))
        
        # Add the new event to single bookings
        self.single_bookings.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)