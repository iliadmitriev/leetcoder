class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even = sum(1 for v in nums1 if v % 2 == 0)
        odd = sum(1 for v in nums1 if v % 2 == 1)

        # array is already have the same parity 
        if even == 0 or odd == 0:
            return True

        # the array is the mixture of odd and even numbers.

        # since can not get rid from all the odd numbers
        # because the last odd number will be the smallest one in the array
        # and to get rid of it we need even smaller 
        # therefore, it is impossible to make all the array numbers even
        # our only chance to make the array odd.
        # to do that we need to have the smallest number to be odd.
        # it must be subtracted from all odd numbers to make them even.
        mi_odd = min(v for v in nums1 if v % 2 == 1) # there are odd number's

        return mi_odd == min(nums1)
        