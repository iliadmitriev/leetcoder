class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        Time: O(n * (n - m))
        """
        def equals(i: int) -> bool:
            """Checks if target starting from i is equal to stamp."""
            for j, ch in enumerate(stamp):
                if not(target[i + j] == "?" or ch == target[i + j]):
                    return False
            return True
        
        # convert string to list of chars
        target = list(target)
        n, m = len(target), len(stamp)
        
        res = []
        visited = set()
        shifted = True
        
        while shifted:
            shifted = False
            for i in range(n - m + 1):
                if i not in visited and equals(i):
                    shifted = True
                    res.append(i)
                    visited.add(i)
                    target[i: i + m] = ['?'] * m
                
        return res[::-1] if all([c == '?' for c in target]) else []