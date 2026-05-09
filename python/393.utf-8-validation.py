class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        c = 0
        for b in data:
            # less or eq 0111 1111
            if b < 128:
                if c:
                    return False
            # less or eq 1011 1111
            elif 128 <= b < 192 :
                if c:
                    c -= 1
                else:
                    return False
            elif 192 <= b < 224:
                if not c:
                    c = 1
                else:
                    return False
            elif 224 <= b < 240:
                if not c:
                    c = 2
                else:
                    return False
            elif 240 <= b < 248:
                if not c:
                    c = 3
                else:
                    return False                
            else:
                return False
        
        return c == 0