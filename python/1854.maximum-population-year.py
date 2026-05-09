

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        population = [0] * 101
        SHIFT = 1950

        for birth, death in logs:
            population[birth - SHIFT] += 1
            population[death - SHIFT] -= 1

        curPopulation, maxPopulation, maxPopYear = 0, 0, 0

        for year, pop in enumerate(population):
            curPopulation += pop

            if curPopulation > maxPopulation:
                maxPopulation = curPopulation
                maxPopYear = year

        return SHIFT + maxPopYear

