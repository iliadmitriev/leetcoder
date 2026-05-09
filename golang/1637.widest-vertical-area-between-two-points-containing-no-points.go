func maxWidthOfVerticalArea(points [][]int) int {
    x := make([]int, len(points))
    for i := 0; i < len(points); i++ {
        x[i] = points[i][0]
    }
    sort.Ints(x)

    delta := x[1] - x[0]
    for i := 2; i < len(points); i++ {
        if x[i] - x[i - 1] > delta {
            delta = x[i] - x[i - 1]
        }
    }
    return delta
}