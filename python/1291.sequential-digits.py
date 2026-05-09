class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Idea:
        Use BFS
        
        1. Init queue with numbers from 1 to 9
        2. Iterate while queue is not empty:
            1. Pop number from queue from start of queue
            2. Check if it fits between low and high, 
                and add it to result
            3. Get least significant digit from number
            4. Append next number to the right
        """
        
        res = []
        
        q = collections.deque(list(range(1,10)))
        
        while q:
            number = q.popleft()
            
            if low <= number <= high:
                res.append(number)
                
            digit = number % 10
            
            if digit < 9:
                q.append(number * 10 + digit + 1)
                    
        return res