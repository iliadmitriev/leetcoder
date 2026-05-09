"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = deque()
        seen = {}

        if node:
            seen[node] = Node(node.val)
            queue.append(node)

        while queue:
            curr = queue.pop()
            for next_node in curr.neighbors:
                if next_node not in seen:
                    seen[next_node] = Node(next_node.val)
                    queue.append(next_node)
                seen[next_node].neighbors.append(seen[curr])
        
        return seen.get(node)
