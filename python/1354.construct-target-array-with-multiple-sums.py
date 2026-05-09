class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """Finds is there a way to construct target array from identity array.
        
        Args:
            target (list of integers): target array to construct.
        
        Returns:
            (bool): True - if there is a way to construct 
                           traget array from identity array
                    False - otherwise
        
        Time: O(n * log n)
        Space: O(n)
                    
        Idea: don't try to build array from matrix. Instead, move backwards and
              try to deconstruct target array down to identity array.
              each step max = max - (sum - max)
              [9, 3, 5] sum = 17, max = 9 => 9 - 8 = 1
              [1, 3, 5] sum = 9, max = 5 => 5 - (9 - 5) = 1
              [1, 3, 1] sum = 5, max = 3 => 3 - (5 - 3) = 1
              [1, 1, 1] sum = 3, max = 1
              
              continue until max > 1 or result of opetation < 1
              if sum == len, and max == 1 => return True
              
              [1, 1, 1, 2] sum = 5, max = 2 => 2 - 3 = -1
              [1, 1, 1, -1] sum = 2, max = 1
              return False
              
              [1, 2, 33] sum = 36, max = 33 => 33 - 3
              [1, 2, 30] 30 - 3
              [1, 2, 27] 27 - 3
              [1, 2, 24]
              use modulus instead substraction
            
        """
        heap = list(map(lambda x: -x, target))
        heapq.heapify(heap)
        curr_sum = sum(target)

        # iterate while biggest number in array is not 1        
        while -heap[0] != 1:

            # get biggest number from array
            max_num = -heapq.heappop(heap)
            # calculate sum of all numbers except biggest
            curr_sum -= max_num

            # if current sum is equal to 1 (case when len of array is equals to 2)
            # we can't proceed (division by 1 is futile)
            if curr_sum == 1:
                return True
            
            # if current sum is 0 or current sum is greater than current biggest number
            if curr_sum == 0:
                return False

            # perform divide
            new_max_num = max_num % curr_sum
            curr_sum += new_max_num

            # if resulted in the same number
            # of even worse result of division is 0
            if new_max_num == 0 or new_max_num == max_num:
                return False
            
            heapq.heappush(heap, -new_max_num)
        
        return True
                        
            
        