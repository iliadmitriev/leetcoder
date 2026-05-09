# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        Idea:
        Greedy algorithm based on postorder iteration with node states.
        
        Node state values (depending on children):
            0 - node has at least one not monitored child
            1 - one of children has a camera and current node in monitored as adjacent
            2 - both children has a camera and current node is monitored as adjacent
            inf - node doesn't have children nodes at all
        
        Node values:
            0 - not monitored
            1 - has camera and monitored
            2 - doesn't have camera and monitored as adjacent
        
        Possible actions:
            state in {2, inf} - do nothing
            state in {0} - add camera, mark node as = 1
            state in {1} - mark as = 2 (monitored as adjacent)
        """
        
        def postorder(x: Optional[TreeNode]) -> Optional[TreeNode]:
            """Postorder recursive iterator"""
            if not x:
                return
            
            yield from postorder(x.left)
            yield from postorder(x.right)
            yield x
        
        res = 0
        for node in postorder(root):
            state = min(
                node.left.val if node.left else float('inf'),
                node.right.val if node.right else float('inf')
            )
            if state == 0:
                res += 1
                node.val = 1
            elif state == 1:
                node.val = 2
            # otherwise state in {2, inf} do nothing
        return res + (root.val == 0)