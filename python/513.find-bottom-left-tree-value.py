# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        que = deque([root])
        res = root.val

        while que:
            
            for i in range(len(que)):
                node = que.popleft()
                if i == 0:
                    res = node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return res

