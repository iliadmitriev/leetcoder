class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Idea: 
            Start from 0 and try to collect target amount using tree approach.
            The bigger coins used to collect target amount the faster it collected using queue.
            We only need the possibility to collect target amount so we will use cache as set
            to not to try to collect same amount more than one time.
            
            Since we use queue, this is an breadth first search.
            On every iteration of BFS counter of coins if increased by 1.
        
        Time: O(amount * len(coins))
        Space: O(amount)
        
        """
        
        
        if amount == 0:
            return 0
        
        cache = set()
        count = 0
        queue = deque([0])
        
        while queue:
            
            count += 1
            
            for _ in range(len(queue)):
                total = queue.popleft()
                
                for coin in coins:
                    next_total = total + coin
                    
                    if next_total in cache:
                        continue
                    if next_total > amount:
                        continue
                    if next_total == amount:
                        return count

                    cache.add(next_total)
                    queue.append(next_total)
                        
        return -1
                    