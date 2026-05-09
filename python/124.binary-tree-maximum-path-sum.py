# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = -float("inf")
        # stack node, is visited
        stack = [(root, False)]
        # store result of calcualtion key = node, value => returning value max single path sum
        cache = {}

        while stack:
            node, vis = stack.pop()
            if vis:
                # get results of previous calculations (and delete them, cause we don't need them anymore)
                left, right = cache.pop(node.left, 0), cache.pop(node.right, 0)
                # calculate single path for current node for with left child, right child, or without
                max_single_path = max(node.val + max(left, right), node.val)
                # recalculate max sum as sum of node value, left and right
                max_sum = max(max_sum, max_single_path, node.val + left + right)
                # return result (save to cache)
                cache[node] = max_single_path

            else:
                # postorder traversal
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return max_sum

