class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Idea:
        
        1) combine two string s and t into one
        2) convert string chars into numbers with ord
        3) xor all the numbers, eliminating numbers which comes in pairs,
           that will leave us single number
        4) covert number back to char with chr

        
        """
        return chr(reduce(operator.xor, map(ord,s + t), 0))