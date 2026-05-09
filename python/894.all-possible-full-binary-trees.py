# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        res = []
        for i in range(2, n, 2):
            left = self.allPossibleFBT(i - 1)
            right = self.allPossibleFBT(n - i)

            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)

        return res