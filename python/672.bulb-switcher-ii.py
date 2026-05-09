class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        """Calculate number of different combinations.
        
        Calculates bulb combinations with number of state changes.
        Possible changes:
        1. Flip all states (XOR with 0xFF...)
        2. Flip only even 2, 4, 6 (XOR with 0xAA...)
        3. Flip only odd 1, 3, 5 (XOR with 0x55...)
        4. Flip every third 1, 4, 7 (XOR with 0x249...)
        
        Idea:
        1. only 3 first bulbs matter (every other bulbs repeat after them)
        2. all operations are commutative (XOR)
        3. there is only 8 possible states for 3 bulbs:
          1(000), 42(001), 3(010), 4(011), 41(100), 2(101), 43(110), (111)
        4. operations is interchangable:
            _ == 11
            1 == 23
            2 == 13
            3 == 12
        
        Args:
            n (int): number of bulbs
            presses (int): number of switch pushes
            
        Returns:
            (int): bulb combinations
        """
        # base cases
        # if we can't switch state,
        # then there is only one possible current combination
        if presses == 0:
            return 1
        
        # if there is only one bulb
        # then no matter how much operations is performed
        # there should be only two states 'on' and 'off'
        if n == 1:
            return 2
        
        
        # if there is two bulbs: 
        # if number of presses is equal to 1,
        # we can only achieve 3 combinations: 1(00), 3 or 4 (01), 2(10)
        # otherwise (if operations more than 1)
        # we can achive any combination of 2 bulbs: 23(00), 12(01), 13(10), 11(11)
        if n == 2:
            if presses == 1:
                return 3
            return 4
        
        # if 3 bulbs and 1 operation:
        # achivable only 4 states: 1(000), 3(010), 4(011), 2(101)
        if presses == 1:
            return 4
        
        # if 3 bulbs and 2 operations:
        # achivable only 7 states: 23(000), 42(001), 3(010), 41(100), 13(101), 43(110), 11(111)
        if presses == 2:
            return 7

        # otherwise every combinations of 3 bulbs is possible which is 2 ^ 3 = 8
        return 8