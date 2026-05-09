class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Optimization 1: if we have enough initial capital to start most expensive project
        # we can choose any k projects from profits
        if w >= max(capital):
            return w + sum(nlargest(k, profits))


        max_profit = []
        # init min capitals heap
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)

        for _ in range(k):

            # while there is still values left in minmal capital heap
            # and there is capital values we can afford
            while min_capital and min_capital[0][0] <= w:
                # get profits from min capitals heap as much as we can
                _, p = heapq.heappop(min_capital)
                # add profits to max profit heap
                heapq.heappush(max_profit, -p)

            # if there is not affordable capitals
            if not max_profit:
                # finish algorithm earlier
                break

            w += -heapq.heappop(max_profit)

        return w