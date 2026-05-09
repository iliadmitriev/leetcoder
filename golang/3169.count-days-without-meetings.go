import (
	"slices"
)

func countDays(days int, meetings [][]int) int {
	slices.SortFunc(meetings, func(a, b []int) int {
		return a[0] - b[0]
	})

	today := 0
	for _, m := range meetings {
		if m[1] <= today {
			continue
		}

		if m[0] > today {
			days -= m[1] - m[0] + 1
		} else {
			days -= m[1] - today
		}

		today = m[1]
	}

	return days
}
