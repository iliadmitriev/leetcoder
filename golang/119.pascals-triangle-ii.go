func getRow(rowIndex int) []int {
    n := rowIndex + 1
    res := make([]int, 0, n)
    curr := 1
    res = append(res, curr)


    for i := 1; i < rowIndex + 1; i++ {
        curr *= n - i
        curr /= i
        res = append(res, curr)
    }

    return res
}