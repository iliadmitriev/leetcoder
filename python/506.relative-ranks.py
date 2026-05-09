class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        places = sorted(range(len(score)), key=score.__getitem__, reverse=True)
        res = [""] * len(score)
        for i in range(len(score)):
            res[places[i]] = str(i + 1)

        if len(score) > 0:
            res[places[0]] = "Gold Medal"

        if len(score) > 1:
            res[places[1]] = "Silver Medal"

        if len(score) > 2:
            res[places[2]] = "Bronze Medal"

        return res

