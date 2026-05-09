# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        Time: O(m + n)
        
        Idea:
        1) Init two stack structures
        2) Inorder tree traversal (while both stacks is not empty):
            a) starting from current root1 append to stack1
               all the left nodes down to the tree leaf
            b) starting from current root2 append to stack2
               all the left nodes down to the tree leaf
            c) check if stack1 top node has less value than stack2,
               then:
               *) pop node from stack1
               *) add node value to result
               *) point root1 to right of popped this node
               otherwise:
               *) pop node from stack2
               *) add node value to result
               *) point root2 to right of popped this node
        3) return result
               
        """
        res = []
        stack1 = deque([])
        stack2 = deque([])
        
        while root1 or root2 or stack1 or stack2:

            while root1:
                stack1.append(root1)
                root1 = root1.left
                
            while root2:
                stack2.append(root2)
                root2 = root2.left
                
                
            if not stack2 or (stack1 and stack1[-1].val < stack2[-1].val):
                root1 = stack1.pop()
                res.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                res.append(root2.val)
                root2 = root2.right

        return res