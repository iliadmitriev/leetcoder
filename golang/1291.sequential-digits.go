func sequentialDigits(low int, high int) []int {
    q := make([]int, 9)
    for i := range q { q[i] = i + 1 }

    res := make([]int, 0)

    for len(q) > 0 {
        num := q[0]
        q = q[1:]

        if low <= num && num <= high {
            res = append(res, num)
        }

        digit := num % 10 + 1
        if digit < 10 && num * 10 + digit <= high {
            q = append(q, num * 10 + digit)
        }
    }

    return res
}