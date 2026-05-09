class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = 0, 0
        for senator in senate:
            if senator == 'R':
                r += 1
            else:
                d += 1

        ban_r, ban_d = 0, 0

        senate = deque(senate)
        while senate:
            sen = senate.popleft()

            if sen == 'R' and r > 0:
                if ban_r > 0:
                    ban_r -= 1
                    continue

                if d > 0:
                    d -= 1
                    ban_d += 1
                    senate.append(sen)
                    continue

                return 'Radiant'

            elif sen == 'D' and d > 0:
                if ban_d > 0:
                    ban_d -= 1
                    continue
                
                if r > 0:
                    r -= 1
                    ban_r += 1
                    senate.append(sen)
                    continue

                return 'Dire'

            # return 'Radiant' if d == 0 else 'Dire'