func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
    m, n := len(firstList), len(secondList)

    res := [][]int{}

    for i, j := 0, 0; i < m && j < n; {
        f := firstList[i]
        s := secondList[j]

        iv, ok := getIntersection(f, s)

        if ok {
            res = append(res, iv)
        }

        if f[1] < s[1] {
            i++
        } else if f[1] > s[1] {
            j++
        } else {
            i++
            j++
        }
    }

    return res
}

func getIntersection(a, b []int) ([]int, bool) {
    m := max(a[0], b[0])
    M := min(a[1], b[1])

    if M >= m {
        return []int{m, M}, true
    }

    return nil, false
}