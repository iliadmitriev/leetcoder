class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return list(range(10))
        
        res = []
        
        def dfs(n: int, num: int) -> None:
            """Calculate all combinations and save them to res.
            
            Ars:
                n (int): depth of recursion.
                num (int): current number.
            """
            # if reached target depth of recursion
            # add current number to results list.
            if n == 0:
                res.append(num)
                return
                
            # least significant digit
            lsd = num % 10
            
            new_lsd = set([lsd - k, lsd + k])
            for next_digit in new_lsd:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    dfs(n - 1, new_num)
                    
        
        for i in range(1, 10):
            dfs(n - 1, i)
        
        return res
                