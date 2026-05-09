func minCost(colors string, neededTime []int) int {
    i, j := 0, 0
    total := 0

    for ;i < len(colors); i = j {
        curMax, curTotal := 0, 0

        for ;j < len(colors) && colors[i] == colors[j]; j++ {
            if neededTime[j] > curMax {
                curMax = neededTime[j]
            }
            curTotal += neededTime[j]
        }

        total += curTotal - curMax
    }

    return total
}