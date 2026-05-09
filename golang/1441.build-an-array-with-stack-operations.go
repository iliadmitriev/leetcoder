func buildArray(target []int, n int) []string {
    res := make([]string, 0)

    for i, cur := 0, 1; i < len(target); cur++ {
        res = append(res, "Push")

        if target[i] == cur {
            i++
        } else {
            res = append(res, "Pop")
        }
    }
    return res
}