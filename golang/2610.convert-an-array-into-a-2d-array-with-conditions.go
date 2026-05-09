func findMatrix(nums []int) [][]int {
    cache := make(map[int]int)
    res := make([][]int, 0)

    var row int
    for _, num := range nums {
        if val, ok := cache[num]; ok {
            row = val + 1
        } else {
            row = 0
        }
        cache[num] = row

        for row >= len(res) {
            res = append(res, make([]int, 0))
        }

        res[row] = append(res[row], num)
    }
    return res
}