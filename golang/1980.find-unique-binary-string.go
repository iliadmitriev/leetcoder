func BinToInt(s string) int {
    res := 0
    for _, ch := range s {
        res *= 2
        res += int(ch - '0')
    }
    return res
}

func IntToBin(x int, n int) string {
    s := make([]byte, n)

    for i := n - 1; i >= 0 ; x, i = x >> 1, i - 1 {
        if x & 1 == 1 {
            s[i] = '1'
        } else {
            s[i] = '0'
        }
    }

    return string(s)
}

func findDifferentBinaryString(nums []string) string {
    n := len(nums[0])

    m := make(map[int]bool)

    for _, num := range nums {
        m[BinToInt(num)] = true
    }
    
    for i := 0; i < (1 << n) + 1; i++ {
        if _, ok := m[i]; !ok {
            return IntToBin(i, n)
        }
    }

    return ""
}