

class Solution:
    def dfs(self, head: ListNode | None, root: TreeNode | None) -> bool:
        if not head:
            return True
        if not root:
            return False
        if head.val == root.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
        return False

    def isSubPath(self, head: ListNode | None, root: TreeNode | None) -> bool:
        if not root:
            return False

        return (
            self.dfs(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )

