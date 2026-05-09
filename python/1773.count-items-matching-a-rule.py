class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        curType = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(x[curType] == ruleValue for x in items)

