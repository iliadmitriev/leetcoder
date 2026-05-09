class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b = 0, 0
        l, r = 0, 0
        while l < len(colors):
            while r < len(colors) and colors[l] == colors[r]:
                r += 1

            if colors[l] == 'A':
                a += max(0, (r - l) - 2)
            else:
                b += max(0, (r - l) - 2)

            l = r
        
        return a > b
        