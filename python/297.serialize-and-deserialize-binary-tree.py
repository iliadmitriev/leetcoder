# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        
        Idea: Use inorder tree traversal for tree node values
        converted to strings to concatenate them with comma
        
        Time: O(n)
        Space: O(log(n))
        n - number of nodes in tree
        """
        # make sure we adding non-empty root to queue
        if not root:
            return ''
        
        res = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(str(None))
        
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        Idea:
        using iterator to iterate all values of input string splited by comma
        build tree with inorder traversing
        """
        if not data:
            return None
        
        values = data.split(',')
        nodes = iter((TreeNode(str(val)) if val != 'None' else None) for val in values)
        
        root = next(nodes)
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            left = next(nodes)
            right = next(nodes)
            if left:
                node.left = left
                queue.append(left)
            if right:
                node.right = right
                queue.append(right)
                
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))