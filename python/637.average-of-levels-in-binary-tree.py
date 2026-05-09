# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        # space: O(log (n))
        count = defaultdict(int)
        total = defaultdict(int)
        
        def average(node: Optional[TreeNode], level: int, cnt: Dict[int, int], tot: Dict[int, int]) -> None:
            if not node:
                return
            
            tot[level] += node.val
            cnt[level] += 1
            
            average(node.left, level + 1, cnt, tot)
            average(node.right, level + 1, cnt, tot)
        
        average(root, 0, count, total)
        
        res = [total[key] / count[key]  for key in sorted(count.keys())]
        
        return res