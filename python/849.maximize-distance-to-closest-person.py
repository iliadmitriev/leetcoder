class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        Idea:
        
        There is three scenarios can happen:
        1. Person can occupy first of seats row, then maximum distance will be distance to next occupied seat
        2. Person can occupy last of seats row, then maximum distance will be distance to previous occupied seat
        3. Person can occupy seat between two occupied seats, then maximum distance will be distance between 
        this occupied seats divided by 2
        """
        # case 1
        res = seats.index(1)
        # case 2
        res = max(res, list(reversed(seats)).index(1))
        # case 3
        # iterate list of seats by groups of 0's and 1's
        for seat, part in itertools.groupby(seats):
            # if seat group consist of 0's
            # then we can seat our person there
            if not seat:
                # calculate if it's a possible maximum
                k = len(list(part))
                res = max(res, (k + 1) // 2)
        
        return res