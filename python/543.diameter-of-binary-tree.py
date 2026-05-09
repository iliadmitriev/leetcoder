# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
    
        stack = [(root, False)]
        ret = {None: -1}

        while stack:
            node, pr = stack.pop()

            if pr:
                left = ret[node.left]
                right = ret[node.right]
                res = max(res, 2 + left + right)
                ret[node] = max(left, right) + 1

            else:
                stack.append((node, True))

                if node.right:
                    stack.append((node.right, False))

                if node.left:
                    stack.append((node.left, False))

        return res