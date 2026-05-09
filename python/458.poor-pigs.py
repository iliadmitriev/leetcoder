class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """Count min number of pigs.
        
        b - number of buckets
        T - number of rounds (minutesToTest // minutesToDie)
        p - number of pigs
        (T + 1) ^ p >= b
        p = log(b) / log(T + 1)
        
        answer is a ceil of p
        """
        return math.ceil( math.log(buckets) / math.log(minutesToTest // minutesToDie + 1) ) 