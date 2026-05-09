# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_idx = {k: v for v, k in enumerate(inorder)}
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            value = preorder.pop(0)
            idx = inorder_idx[value]
            node = TreeNode(value)


            node.left = build(left, idx - 1)
            node.right = build(idx + 1, right)
            
            return node
        
        return build(0, len(preorder) - 1)