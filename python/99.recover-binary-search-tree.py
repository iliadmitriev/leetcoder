# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        Time: O(n)
        Space: O(1)
        """
        if not root:
            return
        
        # first and second nodes to swap
        first, second = None, None
        # previous node pointer
        prev = None
        
        # inorder traversal
        stack = []
        node = root
        while stack or node:
            
            while node:
                stack.append(node)
                node = node.left
        
            node = stack.pop()
            
            # print(prev.val if prev else None, node.val)
            # check if first is not found
            # and previous node is exists
            # and previous node value is greater than next
            if not first and prev and prev.val > node.val:
                first = prev
            
            # if first node is found
            # and previous node is exists
            # and previous node value is greater than next
            if first and prev and prev.val > node.val:
                second = node
            
            # set previous node
            prev = node
            # move pointer right
            node = node.right
        
        # swap nodes
        first.val, second.val = second.val, first.val
                
