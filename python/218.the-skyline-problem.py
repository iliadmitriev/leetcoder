class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        heights = [[1,3,3], [2,4,4], [5,8,2], [6,7,4], [8,9,4]]
        points  = [[1,-3,1], [2,-4,1], [3,3,0], [4,4,0], [5,-2,1], [6,-4,1], [7,4,0], [8,-4,1], [8,2,0], [9,4,0]]
        pq     =  [0, , , , , ,]
        max_height =  0, 3, 4, 0, 2, 4, 2, 4, 0
        res    =  [[1,3], [2,4], [4,0], [5,2], [6,4], [7,2], [8,4], [9, 0]]
        """
        points = []
        for l,r,h in buildings:
            points.append((l, -h, 1))
            points.append((r, h, 0))
        points.sort()
        
        pq = [0]
        max_height = 0
        res = []
        for x, y, pos in points:
            if pos:
                if -y > max_height:
                    max_height = -y
                    res.append((x, -y))
                bisect.insort_right(pq, -y)    
            else:
                pq.pop(bisect.bisect_left(pq, y))
                if max_height > pq[-1]:
                    max_height = pq[-1]
                    res.append((x, max_height))
        return res