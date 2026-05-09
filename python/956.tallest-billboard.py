class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        I. Brute force:
        
        1. Generate all possible combinations of numbers from list.
        Option for every number: 
         - taken to 1st set rod
         - taken to 2nd set 
         - not taken at all.
        2. Generate all the possible lengths for combinations. List of tuples of lengths.
        3. Find two biggest matching lenghts from those tuples.
        O(n^3) - exponential complexity

        II. Meet in the Middle.

        r1, r2, ... rn = list of rods 
        states = {(0,0)} - starting states (left, right) lengths
        * for 1st rod r1: use r1 as left, use r1 as right, not use r1
            states = {(0,0), (r1, 0), (0, r1)}
        * for 2nd rod r2: use r2 as left, use r2 as right, not use r2
            states = {(0,0), (r1, 0), (0, r1), (r2,0), (r1+r2, 0), (r2, r1), (0,r2), (r1, r2), (0, r1+r2)}
        * continue, states grow exponentially
        
        Split list of rods in two halves. (this idea reduces `n` by 2, n // 2)
        And run this algorightm on both parts of the list.
        We will store difference between (left - right) for the first list
        to match difference -(left - right) generated from the second part of the list.

        III. Dynamic programming.

        name two rods not left and right, but shorted and taller, according to their height.
        
        Store:
        
        `dp[taller - shorted] = taller`, or 
        `dp[diff] = taller`, where `shorter = taller - diff`

        store only combinations with max taller height.
        two combiantions of (shorter, taller)
        (2, 3), (0, 1)
        will give only one dp[1] = 3 (dp[diff] = taller)

        """
        dp = {0: 0}
        for rod in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff

                # find all 3 possible combinations 
                # (take to 1st, take to 2nd or don't take, just skip)
                # 1. add to taller
                new_dp[diff + rod] = max(
                    new_dp.get(diff + rod, 0),
                    taller + rod
                )
                # 2. add to shorter
                new_diff = abs(shorter + rod - taller)
                new_taller = max(
                    shorter + rod,
                    taller
                )
                new_dp[new_diff] = max(
                    new_dp.get(new_diff, 0),
                    new_taller
                )
            dp = new_dp
        
        return dp.get(0, 0)
        

