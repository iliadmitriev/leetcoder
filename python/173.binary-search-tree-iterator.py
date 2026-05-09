# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
_SENTINEL = object()

class BSTIterator:
    
    def _traverse(self, root: Optional[TreeNode]) -> List[int]:
        """Convert tree to list recursively starting from root node"""
        if root:
            yield from self._traverse(root.left)
            yield root
            yield from self._traverse(root.right)
            
    def __init__(self, root: Optional[TreeNode]) -> None:
        self.root = root
        self._it = self._traverse(root)
        self._buf = next(self._it, _SENTINEL)

    def next(self) -> int:
        v = self._buf
        self._buf = next(self._it, _SENTINEL)
        if v is _SENTINEL:
            raise StopIteration()
        return v.val

    def __next__(self):
        return self.next()


    def hasNext(self) -> bool:
        return self._buf is not _SENTINEL


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()