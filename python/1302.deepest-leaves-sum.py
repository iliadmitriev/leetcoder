# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        queue = [root]
        prev = []
        
        while queue:
            
            temp = []
            
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                    
            prev, queue = queue, temp
                
                
        return sum(x.val for x in prev)