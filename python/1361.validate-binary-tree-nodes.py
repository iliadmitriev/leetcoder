from itertools import chain
from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find root
        # using counting in order for vetices
        inorder = [0] * n
        for ch in chain(leftChild, rightChild):
            if ch != -1:
                inorder[ch] += 1
        # root vertice should have inorder == 0
        # and there should be only one root
        start = [i for i, cnt in enumerate(inorder) if cnt == 0]
        if len(start) != 1:
            return False

        stack = deque(start)
        vis = [False] * n
        cnt = 0
        vis[start[0]] = True

        while stack:
            node = stack.pop()
            cnt += 1

            if leftChild[node] != -1:
                if vis[leftChild[node]]:
                    return False
                vis[leftChild[node]] = True
                stack.append(leftChild[node])

            if rightChild[node] != -1:
                if vis[rightChild[node]]:
                    return False
                vis[rightChild[node]] = True
                stack.append(rightChild[node])

        return cnt == n