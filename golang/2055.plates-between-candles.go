func left(arr []int, target int) int {
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

func right(arr []int, target int) int {
    lo, hi := 0, len(arr)
    var mid int
    for lo < hi {
        mid = (lo + hi) / 2
        if arr[mid] <= target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

func platesBetweenCandles(s string, queries [][]int) []int {
    // '**|***|**|'
    // build slice of pipe indices -> (2, 6, 9)
    // build slice of star counts -> (2, 3, 2)
    indices := make([]int, 0, len(s))
    counts := make([]int, 0, len(s))
    currCount := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '*' {
            currCount++
        } else if s[i] == '|' {
            counts = append(counts, currCount)
            indices = append(indices, i)
            currCount = 0
        }
    }
    // convert slice of start counts to accumulated 1,2,5,3 -> 1,3,8,11
    for i := 1; i < len(counts); i++ {
        counts[i] += counts[i - 1]
    }
    // process all queries
    res := make([]int, len(queries))
    for i, q := range queries {
        l := left(indices, q[0])
        r := right(indices, q[1])
        if l < len(counts) && l < r {
            res[i] = counts[r - 1] - counts[l]
        }
    }
    return res
}