# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        stack = [(root, False)]
        cache = {}
        while stack:
            node, vis = stack.pop()
            if vis:
                left = cache.pop(node.left, (0,0))
                right = cache.pop(node.right, (0,0))
                cache[node] = (left[1] + right[1] + node.val, max(left) + max(right))
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        
        return max(cache.pop(root))
    