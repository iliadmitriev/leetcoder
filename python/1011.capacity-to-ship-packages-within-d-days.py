class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # lower bound is max weight of single package
        # upper bound is the total weight of all packages (1 day delivery)
        lower, upper = max(weights), sum(weights)

        # use binary search to find value
        while lower < upper:
            mid = (lower + upper) // 2

            # calculate cnt of days needed to deliver all the packages
            # with 'mid' weight capacity
            cnt = 1
            cargo = 0
            for weight in weights:
                if cargo + weight <= mid:
                    cargo += weight
                else:
                    cnt += 1
                    cargo = weight
            
            # if we spend days more than limit
            if cnt > days:
                # increase weight capacity (move lower bound)
                lower = mid + 1
            else:
                # otherwise, decrease weight capacity (move upper bound)
                upper = mid

        return lower
