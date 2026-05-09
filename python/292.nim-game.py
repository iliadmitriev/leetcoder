class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        1 - win
        2 - win
        3 - win
        4 - lost
        5 - win
        6 - win
        """
        return n % 4 != 0

