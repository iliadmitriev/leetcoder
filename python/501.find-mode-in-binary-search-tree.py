from typing import Optional, Iterator, List
from collections import Counter


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node: Optional[TreeNode]) -> Iterator:
            if not node:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        counter, max_counter = 0, 0
        prev = None
        res = []
        for node in inorder(root):
            if prev == node:
                counter += 1
            else:
                counter = 1
            if counter > max_counter:
                res = [node]
                max_counter = counter
            elif counter == max_counter:
                res.append(node)
            prev = node
        return res


        