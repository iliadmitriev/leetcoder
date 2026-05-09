import (
	"sort"
	"strconv"
)

func findMinDifference(timePoints []string) int {
	const day = 24 * 60

	n := len(timePoints)
	times := make([]int, 0, n)

	for _, time := range timePoints {
		h, _ := strconv.Atoi(time[0:2])
		m, _ := strconv.Atoi(time[3:5])
		times = append(times, 60*h+m)
	}
	sort.Ints(times)

	minDiff := day
	for i := 1; i < n; i++ {
		minDiff = min(minDiff, times[i]-times[i-1])
	}

	return min(minDiff, (day-times[n-1]+times[0])%day)
}
