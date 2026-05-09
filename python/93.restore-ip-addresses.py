class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def is_valid(part: str):
            return bool(part) and not(part[0] == "0" and part != "0") and int(part) <= 255
        
        def ip_is_valid(ip: List[str]):
            return all(is_valid(num) for num in ip)

        # C = n! / (k! * (n - k)!)
        # C = 19 * 18 * 17 / (3!) = 969 combinations
        for i, j, k in itertools.combinations(range(1, n), 3):
            ip = [s[:i], s[i:j], s[j:k], s[k:]]
            if ip_is_valid(ip):
                res.append(".".join(ip))

        return res
