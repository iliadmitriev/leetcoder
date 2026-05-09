class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        Find all the Hamiltonian paths in a graph
        (a path in an undirected or directed graph that visits each node exactly once)
        https://en.wikipedia.org/wiki/Hamiltonian_path_problem

        Time: O(3^n) - 3 edges at a vertex (4 ways to go, but you can't walk back)
        Space: O(n) - additinal memory to store set of node coordinates to visit, stack to store visited cells
        """
        # board dimensions limits y and x
        m, n = len(grid), len(grid[0])
        # set of all nodes to visit (tends to empty if we approach to the solution)
        to_visit = set()
        # build set of all nodes,
        # find starting and finishing nodes
        start, finish = None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    to_visit.add((i, j))
                elif grid[i][j] == 2:
                    finish = (i, j)
                    to_visit.add((i, j))
                elif grid[i][j] == 1:
                    start = (i, j)
                    to_visit.add((i, j))

        def walk(pos):
            """Generator yields all the possible ways to go from position pos
            in 4 directional walk, respecting the grid edges m and n.
                pos: tuple y, x
            """
            y0, x0 = pos
            for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
                y, x = y0 + dy, x0 + dx
                if 0 <= y < m and 0 <= x < n:
                    yield y, x

        # result counter
        res = 0
        # use stack for DFS algorithm
        # put starting position to a stack, along with a visited marker
        stack = [(start, False)]
        stack_len = 1
        while stack:
            stack_len = max(stack_len, len(stack))
            pos, vis = stack.pop()
        
            # if node is visted
            if vis:
                # if this node is finishing node and there is no nodes to visit
                # which means all the cells on the grid is visited 
                # increase result counter
                if pos == finish and not to_visit:
                    res += 1
                # put node back to set of nodes to visit.
                to_visit.add(pos)

            else:
                # set node status to visited and put it back to stack
                stack.append((pos, True))
                # remove node from the set of all nodes to visit
                to_visit.remove(pos)
                # add all the neighbor nodes to top of the the stack, with not visited marker
                for step in walk(pos):
                    if step in to_visit:
                        stack.append((step, False))
           
        return res