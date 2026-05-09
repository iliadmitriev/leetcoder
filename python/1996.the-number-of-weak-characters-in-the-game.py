class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        weak = 0
        max_defense = 0
        for _, defense in properties:
            if defense < max_defense:
                weak +=1
            else:
                max_defense = defense
        return weak