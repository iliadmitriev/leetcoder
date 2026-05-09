# Definition for a binary tree node.


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        queue: deque[tuple[TreeNode, Optional[TreeNode]]] = deque([(root, None)])

        while queue:

            size = len(queue)
            parent_x, parent_y = None, None

            for _ in range(size):
                node, parent = queue.popleft()

                if x == node.val:
                    parent_x = parent

                if y == node.val:
                    parent_y = parent

                if parent_x and parent_y:
                    return parent_x != parent_y

                if node.left:
                    queue.append((node.left, node))

                if node.right:
                    queue.append((node.right, node))

        return False

