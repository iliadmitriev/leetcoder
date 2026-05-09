const MOD = int(1e9) + 7

func rev(x int) int {
    y := 0
    for x > 0 {
        y *= 10
        y += x % 10
        x /= 10
    }
    return y
}

func countNicePairs(nums []int) int {
    count := 0
    freq := make(map[int]int, len(nums))

    for _, num := range nums {
        freq[num - rev(num)]++
    }

    for _, n := range freq {
        count += (n * (n - 1)) / 2
    }

    return count % MOD
}