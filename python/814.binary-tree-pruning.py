# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # set fake parent node
        base = TreeNode()
        base.left = root
        # stack of tuples (seen, node, parent, direction link)
        stack = [(False, root, base, 'left')]
        while stack:
            seen, node, parent, link = stack.pop()
            if not seen:
                # put node back for postorder traversal
                stack.append((True, node, parent, link))
                if node.left:
                    stack.append((False, node.left, node, 'left'))
                if node.right:
                    stack.append((False, node.right, node, 'right'))
            else:
                if node.val == 0 and not node.left and not node.right:
                    # delete node (set parents link to none)
                    setattr(parent, link, None)
        
        return base.left