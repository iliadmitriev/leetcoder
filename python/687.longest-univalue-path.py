# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.length = 0
        def dfs(node: Optional[TreeNode], parent: TreeNode) -> int:

            if not node:
                return 0

            left = dfs(node.left, node)
            right = dfs(node.right, node)
            
            self.length = max(self.length, left + right)

            if node.val == parent.val:
                return max(left, right) + 1 
            else:
                return 0
    
        dfs(root, TreeNode(None))

        return self.length