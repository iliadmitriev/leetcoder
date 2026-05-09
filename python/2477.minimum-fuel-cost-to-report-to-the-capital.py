class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        edge_count = [0] * n
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
            edge_count[a] += 1
            edge_count[b] += 1

        # passengers for nodes
        passengers = [1] * n
        # total spend fuel
        fuel = 0
        # init queue and add to queue all children nodes
        # (with edge count == 1 and not root node, starts from 1)
        queue = deque(node for node in range(1, n) if edge_count[node] == 1)
        # start level order BFS from children nodes to root node
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                # add to fuel spent count number of arrived vehicles
                fuel += ceil(passengers[node] / seats)
                
                for nxt in graph[node]:
                    # collect all arrived passengers from current node to parent
                    passengers[nxt] += passengers[node]
                    # use one edge of node (decrease not used edges count)
                    edge_count[nxt] -= 1
                    # if all the edges of next node is used
                    # (except for one the edge connecting to parent)
                    # and node is not root
                    if edge_count[nxt] == 1 and nxt != 0:
                        # add parent node to qeueue
                        queue.append(nxt)

        return fuel
