class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = 0
        divider = 1
        res = 1

        for pos in corridor:
            if seats == 2:
                if pos == 'S':
                    seats = 1
                    res = (res * divider) % MOD
                    divider = 1
                else:
                    divider += 1
            else:
                if pos == 'S':
                    seats += 1

        
        if seats != 2:
            return 0
        
        return res