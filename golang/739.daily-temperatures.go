func dailyTemperatures(temperatures []int) []int {
    n := len(temperatures)
    res := make([]int, n)

    st := make([]int, 0, n)

    for j, tmp := range temperatures {
        // if temperature is rising - update res with current day
        for len(st) > 0 && temperatures[st[len(st) - 1]] < tmp {
            top := st[len(st) - 1]
            res[top] = j - top
            st = st[:len(st) - 1]
        }
        st = append(st, j)
    }

    return res
}