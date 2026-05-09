# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node: TreeNode, lower: int) -> int:
            if not node:
                return 0
            
            res = 0
            
            if node.val >= lower:
                res += 1
                lower = node.val
                
            res += dfs(node.left, lower) + dfs(node.right, lower)
            
            return res
        
        return dfs(root, -inf)