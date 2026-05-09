# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        res = cur = TreeNode()
        node = root
        
        while node:
            if node.left:
                # look for rightmost empty space place of left node
                cand = node.left
                while cand.right:
                    cand = cand.right
                # attache node to rightmost empty space
                cand.right = node
                # move node pointer left
                node = node.left
                # remove left link of right candidate
                cand.right.left = None
            else:
                cur.right = node
                cur = cur.right
                node = node.right
        
        return res.right