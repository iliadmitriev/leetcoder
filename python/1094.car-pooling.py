import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """Emulate trip with load and unload passangers (saving their arrival stop)

        """
        # store passengers arrival in heap
        # item (to, count)
        arrive_heap = []
        # current loaded passangers
        loaded = 0
        
        # iterate all trips sorted in orber by from index
        for count, frm, to in sorted(trips, key=lambda x: x[1]):
            # add passengers for current trip 
            # to arrival
            heapq.heappush(arrive_heap, (to, count))
            # add passengers to load
            loaded += count
            
            # if we have passengers onboard
            # and some of passengers is arrived on current stop (to <= from)
            # we have to pop all of them
            while arrive_heap and arrive_heap[0][0] <= frm:
                # pop passenger
                arrive = heapq.heappop(arrive_heap)
                # unload passengers count
                loaded -= arrive[1]
            
            # on every step loaded passengers count should be
            # less or equal than capacity
            # other wise return False
            if loaded > capacity:
                return False
            
        return True
    