class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {ch: i for i, ch in enumerate(order)}

        arr = []
        for word in words:
            arr.append([order[ch] for ch in word])
        return arr == sorted(arr)