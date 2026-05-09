from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """
        Idea:

            BFS simultaneosly from all the nodes,
            marking all visited nodes.
            BFS garantees than first finished node is the minimal path.

        Algorithm:

            1. add all nodes with their mask to queue as start nodes with 0 distance
                (mask with only one bit set)
            2. queue:
                2.1. get current node, it's mask and distance from queue
                2.2. if mask is all set to 1's then all nodes visited,
                    so return distance
                2.3. iterate all neighbour nodes from current node
                    2.3.1. check if node is not visited with current mask
                    2.3.2. add node to visited, and add to queue with it's new mask, and new distance + 1

        Complexity:

            For every starting node (n) there is 2^n combination (2 because visited or not):
        
            Time: O(n * 2^n)
            Space: O(n * 2^n)
        
        """
        n = len(graph)
        finish = (1 << n) - 1
        # (node, mask, distance)
        queue = deque((i, 1 << i, 0) for i in range(n))
        # visited (node, mask)
        visited = set((i, 1 << i) for i in range(n))

        while queue:
            node, mask, dist = queue.popleft()

            if mask == finish:
                return dist

            for adj in graph[node]:
                new_mask = mask | (1 << adj)

                if (adj, new_mask) in visited:
                    continue
                
                visited.add((adj, new_mask))
                queue.append((adj, new_mask, dist + 1))

        return float("inf")




