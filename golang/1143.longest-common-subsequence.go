func binSearch(arr []int, target int) int {
    lo, hi := 0, len(arr)
    var mid int

    for lo < hi {
        mid = (lo + hi) / 2

        if arr[mid] < target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }

    return lo
}

func longestCommonSubsequence(text1 string, text2 string) int {
    dp := make([]int, 0)

    t2 := make(map[rune][]int)
    for i, ch := range text2 {
        t2[ch] = append(t2[ch], i)
    }

    for _, ch := range text1 {
        if _, ok := t2[ch]; !ok {
            continue
        }

        for i := len(t2[ch]) - 1; i >= 0; i-- {
            idx := t2[ch][i]

            i := binSearch(dp, idx)

            if i == len(dp) {
                dp = append(dp, idx)
            } else {
                dp[i] = idx
            }
        }

    }

    return len(dp)
}