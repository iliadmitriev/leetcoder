class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        order = set()
        for _from, _ in paths:
            order.add(_from)

        for _, _to in paths:
            if _to not in order:
                return _to

        return ""