class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """Find furthest reachable building.
        
        Idea:
        if next building is lower or the same height (delta < 0) as the current just jump on in.
        use priority queue to save height deltas to cover most height with ladders.
        if lenght of queue is greater than ladders then start to spend bricks to
        cover lowes height from the queue.
        if ran out of bricks then current building is furthest. 
        """
        pq = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            
            if d <= 0:
                continue
            
            heapq.heappush(pq, d)
            
            if len(pq) > ladders:
                top = heapq.heappop(pq)
                bricks -= top
            
            if bricks < 0:
                return i
            
        return len(heights) - 1
            