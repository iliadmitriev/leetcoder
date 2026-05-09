# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        LEFT = 'left'
        RIGHT = 'right'
        
        def first_candidate(node: Optional[TreeNode]) -> Optional[TreeNode]:
            while node and (low > node.val or node.val > high):
                node = node.left if node.val > low else node.right
            return node
        
        root = first_candidate(root)
        
        if not root:
            return root
        
        queue = [(root, None, None)]
        while queue:
            node, pred, pos = queue.pop(0)
            node = first_candidate(node)

            if pred:
                setattr(pred, pos, node)

            if node:
                if node.left:
                    queue.append((node.left, node, LEFT))
                if node.right:
                    queue.append((node.right, node, RIGHT))
                
        return root