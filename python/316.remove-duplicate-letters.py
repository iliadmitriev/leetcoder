class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Time: O(n)
        Space: O(n)
        """
        ## latest pos
        occ = {ch: i for i, ch in enumerate(s)}
        # result stack
        stack = []
        visited = set()
        
        for i, ch in enumerate(s):
            
            # if char is in the stack (we have already added it or didn't pop out)
            if ch in visited:
                continue
            
            # if current char is lexicographically larger 
            # than the char in the top of the stack
            # and we still have more of these chars remaining
            # so we can pop it to be later added in the future iterations
            while stack and stack[-1] > ch and occ[stack[-1]] > i:
                # pop from the stack
                visited.remove(stack.pop())
                
            # add char to the top of the stack
            stack.append(ch)
            visited.add(ch)
        
        # return all stack chars joined together
        return ''.join(stack)