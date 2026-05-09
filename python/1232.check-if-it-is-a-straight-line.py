class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        y = s * x + q
        
        s = (y2 - y1) / (x2 - x1)
        q = y - s * x
        
        if x1 == x2 and y1 != y2:
            line is vertical, it's equation is x = x1        

        """

        it = iter(coordinates)
        (x1, y1), (x2, y2) = next(it), next(it)
        for x, y in it:
            if (y2 - y1) * (x - x2) != (y - y2) * (x2 - x1):
                return False

        return True