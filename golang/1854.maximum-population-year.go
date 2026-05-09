import (
	"sort"
)

func maximumPopulation(logs [][]int) int {
	maxYear, curPopulation, maxPopulation := 0, 0, 0
	population := make([][2]int, 0, len(logs)*2)
	for _, log := range logs {
		population = append(population, [2]int{log[0], 1})
		population = append(population, [2]int{log[1], -1})
	}

	sort.Slice(population, func(i, j int) bool {
		if population[i][0] < population[j][0] {
			return true
		}

		return population[i][0] == population[j][0] && population[i][1] < population[j][1]
	})

	for _, pop := range population {
		curPopulation += pop[1]

		if curPopulation > maxPopulation {
			maxYear, maxPopulation = pop[0], curPopulation
		}
	}

	return maxYear
}
