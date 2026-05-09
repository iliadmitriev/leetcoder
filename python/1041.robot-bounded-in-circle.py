class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        Time: O(N)
        Space: O(1)
        
             N
             ^ y
             |    x
        W -------> E
             |
             S
           
        di (directions):
        N 0 -> ( 0,  1)
        W 1 -> (-1,  0)
        S 2 -> ( 0, -1)
        E 3 -> ( 1,  0)
        
        Rotations:
        L (ccw) -> (di + 1) % 4
        R (cw)  -> (di - 1) % 4
        
        Condition:
        * Return back to strting point
        * Not to face North 
        
        """
        di = 0  # face north
        x, y = 0, 0  # postion at 0, 0
        
        for i in instructions:
            if   i == 'L':
                di = (di + 1) % 4  # change direction by 90 deg counter clockwise
            elif i == 'R':
                di = (di - 1) % 4  # change direction by 90 deg clockwise
            elif i == 'G':
                if   di == 0:
                    y += 1  # go North
                elif di == 1:
                    x -= 1  # go West
                elif di == 2:
                    y -= 1  # go South
                elif di == 3:
                    x += 1  # go East
                    
        # robot infinite path could by limited inside circle in two cases:
        #   * When finished facing notrh at 0, 0
        #   * When finish facing any direction except north (at any point).
        #     In this case, robot will perform either wiggling through origin
        #     (with 2 cycles of instrictions)
        #     either nutations oround origin (with 4 cycles of instrictions)
        return di != 0 or (x == 0 and y == 0)