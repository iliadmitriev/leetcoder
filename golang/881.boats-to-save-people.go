func numRescueBoats(people []int, limit int) int {
	maxWeight := people[0]
	for _, person := range people {
		if maxWeight < person {
			maxWeight = person
		}
	}

	weights := make([]int, maxWeight+1)
	for _, person := range people {
		weights[person]++
	}

	boats := 0
	for left, right := 0, maxWeight; left <= right; {
		for left <= right && weights[left] <= 0 {
			left++
		}

		for left <= right && weights[right] <= 0 {
			right--
		}

		if left > right {
			break
		}

		if left+right <= limit {
			weights[left]--
		}

		weights[right]--
		boats++
	}

	return boats
}
