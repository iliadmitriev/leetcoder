class FreqStack:

    def __init__(self):
        # priority queue
        self.heap = []
        # current index
        self.idx = 0
        # count frequency
        self.cnt = defaultdict(lambda:0)
        
    def push(self, val: int) -> None:
        self.cnt[val] += 1
        self.idx += 1
        heapq.heappush(self.heap, (-self.cnt[val], -self.idx, val))
        
    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val