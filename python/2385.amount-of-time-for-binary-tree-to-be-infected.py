# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def dfs(gr: dict[int, list[int]], n: int, start: int) -> int:
            
            vis = set()
            vis.add(start)

            level = -1
            queue = deque([start])

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    for child in gr[node]:
                        if child in vis:
                            continue
                        vis.add(child)
                        queue.append(child)
                level += 1

            return level


        def build_gr(root: Optional[TreeNode], gr: dict[int, list[int]]) -> int:
            if not root:
                return 0
            
            count = 0
            stack = [(None, root)]

            while stack:
                parent, node = stack.pop()
                count += 1

                if parent:
                    gr[node.val].append(parent.val)
                    gr[parent.val].append(node.val)

                if node.right:
                    stack.append((node, node.right))
                
                if node.left:
                    stack.append((node, node.left))

            return count

        gr = defaultdict(list)
        n = build_gr(root, gr)

        return dfs(gr, n, start)