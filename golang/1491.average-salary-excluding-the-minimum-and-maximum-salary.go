func average(salary []int) float64 {
    min, max := math.MaxInt, 0
    total, count := 0, -2

    for _, sal := range salary {
        total += sal
        count ++
        if min > sal { min = sal }
        if max < sal { max = sal }
    }

    return float64(total - min - max) / float64(count)
}