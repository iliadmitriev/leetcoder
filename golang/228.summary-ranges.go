import (
    "fmt"
)

func summaryRanges(nums []int) []string {
    cache := make([][2]int, 0, len(nums))

    for _, num := range nums {
        last := len(cache) - 1
        if last >= 0 && cache[last][1] + 1 == num {
            cache[last][1] = num
        } else {
            cache = append(cache, [2]int{num, num})
        }
    }

    intervals := make([]string, 0, len(cache))
    for _, v := range cache {
        if v[0] == v[1] {
            intervals = append(intervals, fmt.Sprintf("%d", v[0]))
        } else {
            intervals = append(intervals, fmt.Sprintf("%d->%d", v[0], v[1]))
        }
    }

    return intervals
}