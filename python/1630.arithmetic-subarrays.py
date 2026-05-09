class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_arithmetic(arr: List[int]) -> bool:
            lo, hi = min(arr), max(arr)

            if (hi - lo) % (len(arr) - 1) != 0:
                return False
            
            diff = (hi - lo) // (len(arr) - 1)

            if diff == 0:
                if arr != [arr[0]] * len(arr):
                    return False
                return True

            check = [False] * len(arr)
            for n in arr:
                if (n - lo) % diff != 0:
                    return False
                check[(n - lo) // diff] = True
            
            return all(check)

        res = [False] * len(min(l, r))
        for i, (left, right) in enumerate(zip(l, r)):
            res[i] = is_arithmetic(nums[left: right + 1])

        return res