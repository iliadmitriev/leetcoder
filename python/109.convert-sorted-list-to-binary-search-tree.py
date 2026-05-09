# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp = []
        while head:
            temp.append(head)
            head = head.next
        n = len(temp)

        if n == 0:
            return None
        res = TreeNode(None)

        # left bound, right bound, parent link, parent link posittion (default left)
        stack = [(0, n, res, "left")]

        while stack:
            left, right, parent, pos = stack.pop()

            if left == right:
                continue

            mid = (left + right) // 2
            node = TreeNode(temp[mid].val)

            setattr(parent, pos, node)
            stack.append((left, mid, node, "left"))
            stack.append((mid + 1, right, node, "right"))

        return res.left            