class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        Idea:
        1) While current min is odd try to increase it (by multiplying it by 2) until it becomes even
        2) While current max is even try to decsease it (by dividing it by 2) until it becomes odd
        3) Use min heap and max heap (for organazing data)
        since python doesn't have max heap, use min heap with all values negated
        
        Algorithm:
        1. calculate current maximum and deviation
        2. build minimum heap from a given list
        3. iterate while current minimum value from the top of the heap is odd:
            * pop current minimum value
            * multiply value by 2
            * push back to minimum heap
            * check if new multiplyed value become a new maximum (recalculate maximum)
            * recalculate deviation (with new maximum and new minimum from the top of the heap)
        4. calculate current minimum (get it from minimum heap)
        5. build maximum heap from a minimum head (use negative numbers to make minimum heap maximum)
        6. iterate while current maximum value from the top of the heap is even:
            * pop current maximum value
            * divide it by 2
            * push back to maximum heap
            * check if new divided value become a new minimum (recalculate minimum)
            * recalculate deviation (with new minimum and new maximum from the top of the heap)
        7. return deviation 
        
        Time: O(N * log(N))
        Space: O(N)
        """
        # get current max
        max_num = max(nums)
        # build min heap with minimum value at the top
        min_heap = nums.copy()
        heapq.heapify(min_heap)
        # get current difference between minimal and maximal number
        diff = max_num - min_heap[0]

        # while we have minimal odd values at the top of the heap
        # multiply it by 2, recalculate current maximum and put it back to heap
        # recalculate minimal difference
        while min_heap[0] % 2 == 1:
            max_num = max(max_num, min_heap[0] * 2)
            heapq.heapreplace(min_heap, min_heap[0] * 2)
            diff = min(diff, max_num - min_heap[0])

        # save min number
        min_num = min_heap[0]
        # build max heap with minimal value at the top
        max_heap = list(map(lambda x: -x, min_heap))
        heapq.heapify(max_heap)

        # while we have even value at the top of max heap
        # divide it by 2, recalculate current minimum and put it back to heap
        # recalculate minimal difference
        while max_heap[0] % 2 == 0:  # neagative and positive parts of axis is symmetrical (we can get rmainder of a negative number)
            min_num = min(min_num, -max_heap[0] // 2)
            heapq.heapreplace(max_heap, max_heap[0] // 2) # divide it as negative (it's even), and put it back to heap as negative
            diff = min(diff, -max_heap[0] - min_num)

        return diff

