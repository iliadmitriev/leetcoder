class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        le, ge = True, True
        for n1, n2 in pairwise(nums):
            if n1 < n2:
                ge = False
            
            if n1 > n2:
                le = False

            if not ge and not le:
                break

        return le or ge