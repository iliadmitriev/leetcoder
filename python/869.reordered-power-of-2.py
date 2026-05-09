class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # precopute and cache values
        # r = 1
        # limit = 10**9
        # values = set()
        # while r <= limit:
        #     values.add(''.join(sorted(str(r))))
        #     r *= 2

            
        values = {'1289', '0134449', '11266777', '23678', '112234778', '16', '4', '0248', '01466788', '0124', '35566', '0122579', '122446', '2', '23334455', '1', '13468', '234455668', '0469', '23', '0145678', '224588', '011237', '46', '0368888', '8', '012356789', '128', '256', '125'}
        
        return ''.join(sorted(str(n))) in values