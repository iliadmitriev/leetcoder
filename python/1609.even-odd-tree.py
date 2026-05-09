# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([root])
        even = False

        while que:
            pre = float('inf') if even else -float('inf')
            for _ in range(len(que)):
                node = que.popleft()

                if even:
                    if node.val % 2 == 1 or pre <= node.val: return False
                else:
                    if node.val % 2 == 0 or pre >= node.val: return False

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

                pre = node.val

            even = not even

        return True