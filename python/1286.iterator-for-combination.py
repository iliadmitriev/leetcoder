class CombinationIterator:


    def __init__(self, characters: str, combinationLength: int) -> None:
        self.combinations = list(map(lambda x: ''.join(x), list(combinations(characters, combinationLength))))
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return self.combinations[self.count - 1]

    def hasNext(self) -> bool:
        return self.count < len(self.combinations)
