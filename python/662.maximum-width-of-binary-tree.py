# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Count max width of given bianry tree.

        Use level order traversal for calculating.
        """
        if not root:
            return 0

        queue = deque([(root, 0)])
        res = 0
        while queue:

            res = max(res, queue[-1][1] - queue[0][1] + 1)

            for _ in range(len(queue)):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * idx + 1))
                if node.right:
                    queue.append((node.right, 2 * idx + 2))

        return res