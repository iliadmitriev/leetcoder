import (
    "sort"
)

func merge(intervals [][]int) [][]int {
    n := len(intervals)

    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    res := [][]int{intervals[0]}

    for i := 1; i < n; i++ {
        cur := intervals[i]
        last := len(res) - 1

        if last >= 0 && res[last][1] >= cur[0] {
            res[last][1] = max(res[last][1], cur[1])
        } else {
            res = append(res, cur)
        }
    }

    return res
}