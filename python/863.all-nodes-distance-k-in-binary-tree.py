# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        stack = [(root, None)]
        graph = defaultdict(list)

        while stack:
            node, parent = stack.pop()
            if parent:
                graph[parent].append(node)
                graph[node].append(parent)
            if node.right:
                stack.append((node.right, node))
            if node.left:
                stack.append((node.left, node))

        queue = deque([target])
        vis = {target}
        level = 0

        while queue:

            if level == k:
                return list(map(lambda x: x.val, queue))

            for _ in range(len(queue)):
                        
                node = queue.popleft()

                for child in graph[node]:
                    if child not in vis:
                        queue.append(child)
                        vis.add(child)

            level += 1

        return []