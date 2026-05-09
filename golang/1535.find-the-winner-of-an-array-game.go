func getWinner(arr []int, k int) int {
    if k == 1 {
        return max(arr[0], arr[1])
    }

    if k >= len(arr) {
        return maxArr(arr)
    }

    curMax := arr[0]
    curCnt := 0

    for i := 1; i < len(arr); i++ {
        if curMax > arr[i] {
            curCnt++
        } else {
            curCnt = 1
            curMax = arr[i]
        }

        if curCnt == k {
            return curMax
        }
    }
    return curMax
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func maxArr(arr []int) int {
    cur := arr[0]
    for _, v := range arr {
        cur = max(cur, v)
    }
    return cur
}