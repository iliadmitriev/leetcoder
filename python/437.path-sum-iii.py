# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.cache = defaultdict(int)
        self.paths = 0

        def dfs(node: Optional[TreeNode], curr):
            if not node:
                return 0

            node_sum = curr + node.val
            self.paths += self.cache[node_sum]

            self.cache[node_sum + targetSum] += 1
            dfs(node.left, node_sum)
            dfs(node.right, node_sum)
            self.cache[node_sum + targetSum] -= 1

        self.cache[targetSum] = 1
        dfs(root, 0)
        return self.paths
    
