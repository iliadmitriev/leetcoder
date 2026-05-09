"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
from itertools import chain

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        node = Node(1, False, None, None, None, None)
        if len(set(sum(grid,[]))) == 1:
            node.isLeaf = True
            node.val = grid[0][0]
        else:
            node.topLeft = self.construct([row[:n // 2] for row in grid[:n // 2]])
            node.topRight = self.construct([row[n // 2:] for row in grid[:n // 2]])
            node.bottomLeft = self.construct([row[:n // 2] for row in grid[n // 2:]])
            node.bottomRight = self.construct([row[n // 2:] for row in grid[n // 2:]])

        return node
