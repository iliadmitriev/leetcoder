# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
             return []

        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)  # Base case: Empty tree root

        def copy_with_offset(root: TreeNode, offset: int):
            """Make a tree copy with shift added to all values."""
            if not root or not offset:
                return root
            res = TreeNode()
            queue = deque([(root, res, 'left')])
            while queue:
                node, parent, side = queue.popleft()
                new_node = TreeNode(node.val + offset)
                if parent: setattr(parent, side, new_node)
                if node.left:
                    queue.append((node.left, new_node, 'left'))
                if node.right:
                    queue.append((node.right, new_node, 'right'))
            return res.left
            
        for i in range(1, n + 1):
            for root in range(1, i + 1):
                for left in dp[root - 1]:
                    for right in dp[i - root]:
                        current = TreeNode(root)
                        current.left = left
                        current.right = copy_with_offset(right, root)
                        dp[i].append(current)
        return dp[n]



