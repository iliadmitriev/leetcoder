import "sort"

func minimumBoxes(apple []int, capacity []int) int {
	sort.Ints(capacity)
	appleCount := 0
	for _, ap := range apple {
		appleCount += ap
	}

	count := 0
	for i := len(capacity) - 1; i >= 0 && appleCount > 0; i-- {
		appleCount -= capacity[i]
		count += 1
	}

	return count
}
