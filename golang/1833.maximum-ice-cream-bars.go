import (
	"slices"
)

func maxIceCream(costs []int, coins int) int {
	maxCost := slices.Max(costs)
	counts := make([]int, maxCost+1)
	bars := 0

	for _, cost := range costs {
		counts[cost]++
	}

	for cost := 1; cost <= maxCost; cost++ {
		if counts[cost] == 0 {
			continue
		}

		canBuy := min(counts[cost], coins/cost)
		coins -= cost * canBuy
		bars += canBuy

		if coins < cost {
			break
		}
	}

	return bars
}