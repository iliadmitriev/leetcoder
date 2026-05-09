class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        def digitize(num: int) -> list[int]:
            res: list[int] = []
            while num:
                num, r = divmod(num, 10)
                res.append(r)

            return res[::-1]

        res: list[int] = []
        for num in nums:
            res.extend(digitize(num))

        return res

