from bisect import bisect_left

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # minimum is first met number from the begining with non zero frequency
        mn = float(next(i for i in range(256) if count[i]))
        # maximum is first met number from the end with non zero frequency
        mx = float(next(i for i in range(255, -1, -1) if count[i]))
        n, total = 0, 0
        max_count, mode = 0, 0
        for value, values_count in enumerate(count):
            n += values_count
            total += value * values_count
            if values_count > max_count:
                max_count = values_count
                mode = value
            # convert array to accumulative form
            count[value] = n
        # calculate mean
        mean = float(total / n)
        # find median
        median1 = bisect_left(count, n / 2)
        median2 = bisect_left(count, (n + 1) / 2)
        median = (median1 + median2) / 2
        return [mn, mx, mean, median , mode]
