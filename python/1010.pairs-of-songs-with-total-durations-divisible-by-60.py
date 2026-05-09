class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        1. convert array to array of remainders:
            [30, 20, 150, 100, 40] % 60 --> [30, 20, 30, 40, 40]
            
        2. calculate frequency of elements, and store it to map
            remander -> frequency
            where remainder is between [0, 59] inclusive
        
            [30, 20, 30, 40, 40] --> {20: 1, 30: 2, 40: 2}
            
        3. calcualte number of pairs:
            a) for remanders wich is not 0 or 30:
                for 20 you have to add 40 to get 60,
                so number of combination wich is divisible by 60
                is number of counts 40 multiplied by number of counts 20
                T[20] * T[40], or T[i] * T[60 - i] in general
                
            b) for remainders 0:
                multiply count of 0 remainders with themselft minus 1
                (one is needed to make a pair)
            
            c) for remainder 30:
                multiply count of 30 remainders with themselft minus 1
                but divide it by 2
            
            d) for remainders more than 30:
                they don't need to be calculated, 
                they all have been calculated when in paragraph a
                
        """
        T = collections.Counter([i % 60 for i in time])
        return sum([T[i] * T[60 - i] for i in range(1, 30)]) + \
                (T[0] * (T[0] - 1) + \
                 T[30] * (T[30] - 1)) // 2

