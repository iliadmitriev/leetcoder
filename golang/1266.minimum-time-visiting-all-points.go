func minTimeToVisitAllPoints(points [][]int) int {
    abs := func (x int) int {
        if x < 0 {
            return -x
        }

        return x
    }

    res := 0

    for i := 1; i < len(points); i++ {
        dx := abs(points[i - 1][0] - points[i][0])
        dy := abs(points[i - 1][1] - points[i][1])

        res += max(dx, dy)
    }

    return res
}