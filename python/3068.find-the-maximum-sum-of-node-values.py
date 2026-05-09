class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        INF = int(1e9)
        inc = 0
        inc_cnt, dec_cnt = 0, 0
        inc_min, dec_min = INF, INF
        total = 0

        for num in nums:
            total += num

            if num ^ k > num:
                inc += (num ^ k) - num
                inc_cnt += 1
                inc_min = min(inc_min, (num ^ k) - num)
            else:
                dec_cnt += 1
                dec_min = min(dec_min, num - (num ^ k))

        if inc_cnt == 0:
            return total

        if inc_cnt % 2 == 0:
            return total + inc

        if dec_cnt == 0:
            return total + inc - inc_min

        return total + inc - min(inc_min, dec_min)

