class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """Calculates minimum cost to move chips
        even moves (-2, +2) is free
        odd moves (-1, +1) cost 1
        
        :param position: list of positions
        """
        odd = sum(map(lambda x: x & 1, position))
                
        return min(odd, len(position) - odd)
    