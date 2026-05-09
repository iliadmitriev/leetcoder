class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Calculate how much time (min) takes to all of fruits
        represented by input matrix to be completely rotten.

        If some of fruites is left fresh then returns -1

        :param grid: 2D matrice (m * n) of fruits with values 0, 1 or 2
        :type grid: List[List[int]]
        :returns: minutes or -1
        :rtype: int
        """
        # result variable
        res = 0
        # set of fruits (coordinates tuples) to be rotting on the next step
        # i.e. ((1,1), (1,2) ... (x,y))
        # where 0 > x > n
        #       0 > y > m
        rotting = set()
        # fresh, set of fresh fruits left to be rotten (coordinates tuples)
        fresh = set()
        # fill initial rotting and fresh sets
        for j, row in enumerate(grid):
            for i, cell in enumerate(row):
                if cell == 2:
                    rotting.add((i, j))
                elif cell == 1:
                    fresh.add((i, j))

        # while there are fresh fruits left and rotting process is going on
        while fresh and rotting:
            rotting = set().union(*[
                fresh.intersection(
                    {(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)}
                ) for i, j in rotting
            ])
            fresh.difference_update(rotting)
            res += 1

        # return -1 if theres is fresh fruits left
        # else return how much time spent
        return -1 if fresh else res
