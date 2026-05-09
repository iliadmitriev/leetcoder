class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        data = sorted(zip(efficiency, speed), reverse=True)
        hq = []
        total_speed = 0
        produce = 0
        for efficiency, speed in data:
            if len(hq) > k - 1:
                total_speed -= heapq.heappop(hq)
            
            heapq.heappush(hq, speed)
            total_speed += speed
            produce = max(produce, total_speed * efficiency)
        
        return produce % (10**9 + 7)