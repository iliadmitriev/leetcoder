class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        counter = 1
        
        for ch in preorder.split(','):
            if counter == 0:
                return False
                    
            counter += -1 if ch == '#' else 1
        
        return counter == 0