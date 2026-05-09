# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def gen_subtrees(node: Optional[TreeNode]):
            stack = [(root, False)]
            cache = {None: "#"}
            while stack:
                node, done = stack.pop()
                if not node:
                    continue

                if done:
                    st = ",".join([
                        str(node.val),
                        cache[node.left],
                        cache[node.right]
                    ])
                    yield st, node
                    cache[node] = st                

                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        res = []
        subtrees = defaultdict(list)
        for subtree, node in gen_subtrees(root):
            if len(subtrees[subtree]) == 1:
                res.append(node)
            subtrees[subtree].append(node)

        return res