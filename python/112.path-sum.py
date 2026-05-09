# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, targetSum)]
        while stack:
            node, target = stack.pop()
            
            target -= node.val
            
            if  target == 0 and not node.left and not node.right:
                return True
            
            if node.left:
                stack.append((node.left, target))
                
            if node.right:
                stack.append((node.right, target))
                
        return False