class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def step(tape: str) -> str:
            skip = 0
            for ch in reversed(tape):
                if ch == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield ch
        
        for a, b in itertools.zip_longest(step(s), step(t)):
            if a != b:
                return False
        
        return True
    