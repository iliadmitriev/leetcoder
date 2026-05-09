class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = Counter(map(lambda x: x[0], matches))
        losses = Counter(map(lambda x: x[1], matches))
        zero, one = set(), set()
        
        for player, _ in wins.items():
            if losses[player] == 0:
                zero.add(player)
            elif losses[player] == 1:
                one.add(player)

        for player, loss in losses.items():
            if loss == 1:
                one.add(player)

        return [sorted(zero), sorted(one)]