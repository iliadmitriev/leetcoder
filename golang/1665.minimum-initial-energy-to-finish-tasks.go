import (
  "cmp"
	"slices"
)

func minimumEffort(tasks [][]int) int {
	slices.SortFunc(tasks, func(a, b []int) int {
		return cmp.Compare(a[1] - a[0], b[1] - b[0])
	})

	res := 0

	for _, task := range tasks {
		res = max(task[1], res+task[0])
	}

	return res
}