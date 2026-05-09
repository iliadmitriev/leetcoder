from heapq import heapify, heappush, heappop


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # number of opertations
        k = 0

        # total sum of all numbers
        total = sum(nums)
        # target total sum
        target = total / 2

        # max heap queue (min heap of negative numbers)
        hq = list(map(lambda x: -x, nums))
        heapify(hq)

        while target > 0:
            num = -heappop(hq)
            num /= 2
            target -= num
            k += 1
            heappush(hq, -num)

        return k            

