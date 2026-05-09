from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return map(lambda x: x[0], sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k])
