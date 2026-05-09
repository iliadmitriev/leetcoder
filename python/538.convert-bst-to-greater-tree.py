# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        total = 0
        
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return node
            nonlocal total
            
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)
            
        dfs(root)
        return root
    