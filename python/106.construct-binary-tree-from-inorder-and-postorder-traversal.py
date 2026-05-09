# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """   l  *      r
            [ 9, 3, 15, 20, 7]
                            
              l         r   *
            [ 9, 15, 7, 20, 3]
        """
        node_idxs = {node: idx for idx, node in enumerate(inorder)}
        n = len(postorder) - 1
        stack = [(0, n, None)]
        cache = {}

        while stack:

            left, right, node = stack.pop()

            if node:
                if left in cache:
                    node.left = cache.pop(left)
                if right in cache:
                    node.right = cache.pop(right)

            else:
                if not postorder or left > right:
                    continue

                value = postorder.pop()
                node = TreeNode(value)

                idx = node_idxs[value]
                stack.append(((left, idx - 1), (idx + 1, right), node))
                stack.append((left, idx - 1, None))
                stack.append((idx + 1, right, None))
                cache[(left, right)] = node

        return cache.get((0, n))