class Solution:
    def largestInteger(self, num: int) -> int:
        
        parity = []
        even, odd = [], []
        while num:
            d = num % 10
            if d % 2:
                odd.append(d)
                parity.append(False)
            else:
                even.append(d)
                parity.append(True)
            num //= 10
        
        heapify(even), heapify(odd)

        digits = [heappop(even if p else odd) for p in parity]
        while digits:
            num = num * 10 + digits.pop()
        return num

            