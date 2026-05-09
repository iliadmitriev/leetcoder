from bisect import insort_left, bisect_right

class StockSpanner:

    def __init__(self):
        # stack of tuples (price, days span)
        self.stack = []

    def next(self, price: int) -> int:
        # add 1 for days
        days = 1

        # accumulate all the days which price is lower or equal 
        # to the current price popping their values from stack
        while self.stack and self.stack[-1][0] <= price:
            days += self.stack.pop()[1]

        # add to stack current price and accumulated value of days
        # instead of popped values
        self.stack.append((price, days))

        return days
