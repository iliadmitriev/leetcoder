class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        data = [set() for _ in range(26)]
        for word in ideas:
            prefix = ord(word[0]) - 97
            suffix = word[1:]
            data[prefix].add(suffix)

        res = 0
        for i in range(len(data)):
            for j in range(i, len(data)):
                if data[i] and data[j]:
                    inter = len(data[i].intersection(data[j]))
                    res += (len(data[i])  - inter) * (len(data[j]) - inter) * 2

        return res