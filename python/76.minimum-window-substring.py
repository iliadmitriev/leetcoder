class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        
        need = Counter(t)
        window = defaultdict(int)
        fulfilled = 0

        res = ""
        l = 0

        for r in range(m):
    
            if s[r] in need:

                window[s[r]] += 1

                if need[s[r]] >= window[s[r]]:
                    fulfilled += 1

            while fulfilled == n and l <= r:

                if not res or len(res) > (r + 1 - l):
                    res = s[l: r + 1]

                if s[l] in window:
                    window[s[l]] -= 1
                    
                    if need[s[l]] > window[s[l]]:
                        fulfilled -= 1

                l += 1

        return res