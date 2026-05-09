class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = dict()
        
        def helper(i: int) -> bool:
            if i < 0 or i >= len(arr):
                return False
            
            if i in visited:
                return visited[i]
            
            visited[i] = arr[i] == 0
            
            if arr[i] == 0:
                return True
            
            return helper(i - arr[i]) or helper(i + arr[i])
        
        
        return helper(start)
