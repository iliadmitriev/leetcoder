class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """

        Use monotonic decreasing stack.
        Init result array with 0's.
        iterate array left to right.
        while current temperature is greater than top of the stack,
        pop index from stack and add to result the difference between current index.
        put indexes to monotonic decresing stack.

        stack = [ 6, 7 ] <- top
                                             *   
        data = [73, 74, 75, 71, 69, 72, 76, 73]
        idx  = [ 0,  1,  2,  3,  4,  5,  6,  7] 
        res =  [ 1,  1,  4,  2,  1,  1,  0,  0]
        """
        # monotonic decreasing stack
        stack = []
        res = [0] * len(temperatures)
        for curr, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                index = stack.pop()
                res[index] = curr - index
            stack.append(curr)
        return res