class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        first  (n - 1)! sequences start from 1
        second (n - 1)! sequences start from 2
        ...
        """
        # i.e. nums = [1, 2, 3, 4]
        nums = list(map(str, range(1, n + 1)))
        res = []
        # i.e. k = 24
        k -= 1 # shift k to start from 0
        while nums:
            # 3, 5 = 23 divmod 3!
            # 2, 1 = 5 divmod 2!
            # 1, 0 = 1 divmod 1!
            # 0, 0 = 0 divmod 0!
            idx, k = divmod(k, factorial(len(nums) - 1))
            res.append(nums.pop(idx))
        
        return ''.join(res)