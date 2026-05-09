func uniqLen(s string) int {
    cache := [26]bool{}
    res := 0
    for _, ch := range s {
        if cache[ch - 'a'] {
            continue
        }
        cache[ch - 'a'] = true
        res++
    }
    return res
}

func mask(s string) int {
    v := 0
    for _, ch := range s {
        v |= 1 << (ch - 'a')
    }
    return v
}

func maxLength(arr []string) int {
    filtered := make([]string, 0, len(arr))
    for i := range arr {
        if uniqLen(arr[i]) == len(arr[i]) {
            filtered = append(filtered, arr[i])
        }
    }

    masked := make([]int, 0, len(filtered))
    for i := range filtered {
        masked = append(masked, mask(filtered[i]))
    }


    var dp func (int, int) int
    cache := make(map[int]int)
    dp = func (curMask int, curLen int) int {
        if val, ok := cache[curMask]; ok {
            return val
        }

        res := curLen

        for i, msk := range masked {
            if msk & curMask  == 0 {
                newLen := dp(msk | curMask, curLen + len(filtered[i]))
                res = max(res, newLen)
            }
        }

        cache[curMask] = res
        return res
    }

    return dp(0, 0)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
