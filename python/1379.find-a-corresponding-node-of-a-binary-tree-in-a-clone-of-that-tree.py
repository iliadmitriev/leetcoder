# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return
        
        stack = [(original, cloned)]
        
        while stack:
            orig, clnd = stack.pop(0)
            
            if orig == target:
                return clnd
            
            if orig.left:
                stack.append((orig.left, clnd.left))
            if orig.right:
                stack.append((orig.right, clnd.right))
        