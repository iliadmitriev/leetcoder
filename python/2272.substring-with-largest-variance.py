class Solution:
    def largestVariance(self, s: str) -> int:


        result = 0
        count = defaultdict(int)
        index = defaultdict(list)
        for i, ch in enumerate(s):
            count[ch] += 1
            index[ch].append((i, ch))

        # a - minor, b - major
        # flag - we have met minor, and total > 0 is True, False otherwise
        for a, b in itertools.permutations(count.keys(), 2):
            if count[b] - 1 > result:
                total, flag = 0, False
                for i, x in sorted(index[a] + index[b]):
                    if x == a:
                        flag = total > 0
                    if x == a and flag:
                        total -= 1
                    elif x == b:
                        result = max(result, total + flag)
                        total += 1

        return result