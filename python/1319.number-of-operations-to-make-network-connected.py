class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        n - number of nodes (vertices)
        e - number of edges

        if e >= n - 1, problem have a solution (we have enough edges to connect all nodes)
        if e < n - 1, there is no solution

        k - number of components (number of disconnected islands)
        if k == 1 (all vertices are connected) answer is 0
           k == 2 (we have 2 islands) answer is 1 (we need 1 edge to connect these islands)
           k == 3, answer is 2

           general answer is k - 1
        """
        if len(connections) < n - 1:
            return -1
        
        parent = list(range(n))
        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                parent[parent_y] = parent_x

        # join all connected nodes
        for u, v in connections:
            union(u, v)

        # compress paths
        parent = [find(node) for node in parent]

        # count unique parent nodes (connected components)
        k = len(set(parent))

        return k - 1

