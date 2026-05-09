# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        stack = [(root, False)]
        res = ""
        
        while stack:
            node, seen = stack.pop()
            if seen:
                res += ')'
            else:
                stack.append((node, True))
                
                res += "(" + str(node.val)
                
                if not node.left and node.right:
                    res += "()"
                    
                if node.right:
                    stack.append((node.right, False))
                    
                if node.left:
                    stack.append((node.left, False))
                    
        return res[1:-1]