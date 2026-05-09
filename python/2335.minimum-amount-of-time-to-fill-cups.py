class Solution:
    def fillCups(self, amount: List[int]) -> int:
        """
        [1,4,2]        [5,4,4]        [5,0,0]
        [1,3,2]        [4,3,4]        [4,0,0]
        [1,2,1]        [3,3,3]        [3,0,0]
        [0,1,1]        [2,2,3]        [2,0,0]
        [0,0,0]        [2,1,2]        [1,0,0]
                       [1,1,1]        [0,0,0]
                       [0,1,0]
                       [0,0,0]
        """
        step = 0
        amount = [-a for a in amount if a > 0]
        heapify(amount)
        while len(amount) >= 2:
            val1, val2 = -heappop(amount) - 1, -heappop(amount) - 1
            if val1 > 0: heappush(amount, -val1)
            if val2 > 0: heappush(amount, -val2)
            step += 1
        if len(amount) == 1:
            step += -amount.pop()
        return step

