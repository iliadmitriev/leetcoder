

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def dfs(node: TreeNode | None, depth: int) -> tuple[int, list[int]]:
            if not node:
                return 0, []

            if not node.left and not node.right:
                return 0, [depth]

            leftCount, leftLeaves = dfs(node.left, depth + 1)
            rightCount, rightLeaves = dfs(node.right, depth + 1)

            count = 0
            for left in leftLeaves:
                for right in rightLeaves:
                    if left + right - 2 * depth <= distance:
                        count += 1

            allLeaves: list[int] = []
            for left in leftLeaves:
                if left - depth <= distance:
                    allLeaves.append(left)

            for right in rightLeaves:
                if right - depth <= distance:
                    allLeaves.append(right)

            return count + leftCount + rightCount, allLeaves

        count, *_ = dfs(root, 0)

        return count

