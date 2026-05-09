# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(node: Optional[TreeNode], back: bool = False) -> Optional[TreeNode]:
            stack = [(node, False)]
            while stack:
                node, seen = stack.pop()
                if not node:
                    continue
                if seen:
                    yield node
                else:
                    stack.append((getattr(node, 'left' if back else 'right'), False))
                    stack.append((node, True))
                    stack.append((getattr(node, 'right' if back else 'left'), False))
                        
        fwd, bwd = inorder(root, False), inorder(root, True)
        left, right = next(fwd), next(bwd)
        while left.val < right.val:
            cur = left.val + right.val
            if cur > k:
                right = next(bwd)
            elif cur < k:
                left = next(fwd)
            else:
                return True
        return False