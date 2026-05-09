func maxRunTime(n int, batteries []int) int64 {
    m := len(batteries)
    sort.Ints(batteries)

    extra := 0
    for i := 0; i < m - n; i++ {
        extra += batteries[i]
    }

    live := batteries[m - n:]

    for i := 1; i < n; i++ {
        diff := live[i] - live[i - 1]
        if extra / i < diff {
            return int64(live[i - 1] + extra / i)
        }

        extra -= diff * i
    }

    return int64(live[n - 1] + extra / n)
    
}