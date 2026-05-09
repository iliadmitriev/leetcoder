# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        stack = [(root, False)]
        data = []

        while stack:

            node, ret = stack.pop()
            # value returned
            if ret:
                count = 1
                total = node.val
                
                if node.left:
                    left, count_left = data.pop()
                    total += left
                    count += count_left

                if node.right:
                    right, count_right = data.pop()
                    total += right
                    count += count_right

                if total // count == node.val:
                    res += 1

                # return value
                data.append((total, count))
                continue

            # value not returned
            # postorder traversal (reversed)

            stack.append((node, True))

            if node.right:
                stack.append((node.right, False))

            if node.left:
                stack.append((node.left, False))


        return res 