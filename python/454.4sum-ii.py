class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # map of frequncies sum of all combinations of first and second list
        # Time: O(n^2)
        h_map = Counter(map(sum, itertools.product(nums1, nums2)))
        
        # calculate counterpart 
        # res = reduce(operator.add, map(lambda x: h_map[-x], map(sum, itertools.product(nums3, nums4))), 0)
        
        n = len(nums3)
        res = 0
        for k in range(n):
            for l in range(n):
                res += h_map[0 - nums3[k] - nums4[l]]

        return res