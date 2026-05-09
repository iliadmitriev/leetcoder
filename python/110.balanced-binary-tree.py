# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth_analyze_tuple(node: 'TreeNode') -> tuple[bool, int]:
            if node is None:
                return True, 0

            hl, hr = depth_analyze_tuple(node.left), depth_analyze_tuple(node.right)

            return hl[0] and hr[0] and abs(hr[1] - hl[1]) <= 1,  max(hl[1] + 1, hr[1] + 1)
        return depth_analyze_tuple(root)[0]
