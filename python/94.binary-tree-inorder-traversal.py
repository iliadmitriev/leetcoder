# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node: Optional[TreeNode]) -> Iterator[Optional[TreeNode]]:
            if not root:
                return
            # stack of tuples (node, seen)
            stack = [(root, False)]
            while stack:
                node, seen = stack.pop()
                
                if not node:
                    continue
                
                if not seen:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
                else:
                    yield node.val
                    
        return list(inorder(root))