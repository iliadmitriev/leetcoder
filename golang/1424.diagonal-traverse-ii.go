func findDiagonalOrder(nums [][]int) []int {
    buff := make([][]int, 0)

    m := len(nums)
    size := 0
    var x int

    for i := 0; i < m; i++ {
        n := len(nums[i])
        x = i

        for j := 0; j < n; j++ {
            if len(buff) == x {
                buff = append(buff, make([]int, 0))
            }

            buff[x] = append(buff[x], nums[i][j])
            x++
            size++
        }
    }

    out := make([]int, 0, size)
    for i := 0; i < len(buff); i++ {
        for j := len(buff[i]) - 1; j >= 0; j-- {
            out = append(out, buff[i][j])
        }
    }
    return out
}