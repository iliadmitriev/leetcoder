class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        data = sorted(c.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
        return ''.join(map(lambda x: x[0] * x[1], data))