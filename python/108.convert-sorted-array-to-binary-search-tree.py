# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not (length := len(nums)):
            return None

        # we will store our result as a left node of res
        res = TreeNode()
        # we put to the top of stack values:
        # - left and right list bounds
        # - link to parent
        # - and branch of parent
        stack = [(0, length, res, 'left')]
        # while stack is not empty
        while stack:
            l, r, parent, side = stack.pop()
            # check if left and right bounds match
            # colloquially, array slice is empty,
            # we just skip iteration
            if l == r:
                continue
            # create current node from the middle element of sorted array
            curr = TreeNode(nums[(r + l) // 2])
            # set parent link (left or right) to current created node
            setattr(parent, side, curr)

            # slice array in two half in the middle
            # append left and right bounds for array slices to stack
            # with current node as parent
            stack.append((l, (r + l) // 2, curr, 'left'))
            stack.append(((r + l) // 2 + 1, r, curr, 'right'))

        return res.left
