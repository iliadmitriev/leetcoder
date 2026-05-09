class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        specials = {".", "..", ""}
        res = []
        for chunk in path:
            if chunk not in specials:
                res.append(chunk)
            elif chunk == ".." and res:
                res.pop()
        return "/" + "/".join(res)