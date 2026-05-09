# Definition for a binary tree node.


import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        q = collections.deque()
        q.append(root)
        level = 1

        maxSum = root.val
        maxLevel = 1

        while q:
            cur = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            if cur > maxSum:
                maxSum = cur
                maxLevel = level

            level += 1

        return maxLevel

