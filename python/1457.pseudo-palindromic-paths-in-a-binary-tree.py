# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        Idea:
        1) traverse tree with preorder dfs algorithm
        2) save character frequency (parity), if a path is palindrome
           all but one characted should have even parity
        3) optimization: since value is between 1 and 9 compress path to bitmask
        """
        if not root:
            return 0
        
        stack = [(root, 0)]
        palindrome_count = 0
        
        while stack:
            
            node, data = stack.pop()

            data ^= (1 << node.val)

            if not node.left and not node.right:
                if data & (data - 1) == 0:
                    palindrome_count += 1
                    
            if node.left:
                stack.append((node.left, data))
            if node.right:
                stack.append((node.right, data))
            
        return palindrome_count
        